import random
from string import ascii_uppercase, digits

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import PlayerForm
from .models import Games, Players

MAX_HEALTH = 10


def lobby(request):
    # Create Game
    # Join Game
    return HttpResponse("Yer not a wizard yet, 'Arry! Welcome to the Lobby. Check back soon.")


def create_player(request, shortcode):
    form = PlayerForm(request.POST or None)
    if form.is_valid():
        player = form.save(commit=False)
        player.game = Games.objects.get(shortcode=shortcode)
        player.save()
        messages.success(request, 'Added Player')
        return redirect('active-game', shortcode=shortcode)
    return render(request, 'HPHBhelper/form.html', {'form': form, 'shortcode': shortcode})


def active_game(request, shortcode):
    game = Games.objects.get(shortcode=shortcode)
    active_players = Players.objects.filter(game=game)

    post = request.POST
    if 'player_id' in post:
        # form submitted
        player_to_modify = Players.objects.get(pk=post['player_id'])
        if 'stunned' in post:
            player_to_modify.health = 10
            player_to_modify.coins = 0
            player_to_modify.damage_tokens = 0
        elif 'end_turn' in post:
            player_to_modify.coins = 0
            player_to_modify.damage_tokens = 0
        else:
            player_to_modify.health += int(post.get('health', 0))
            player_to_modify.coins += int(post.get('coins', 0))
            player_to_modify.damage_tokens += int(post.get('damage_tokens', 0))
        player_to_modify.save()

    return render(request, 'HPHBhelper/game.html',
                  {'shortcode': shortcode,
                   'active_players': active_players,
                   'max_health': MAX_HEALTH})


def create_game(request):
    letters = 'ABCDEFGHJKLMNPQRSTUVWXYZ1234567890'
    # letters = ascii_uppercase + digits
    active_games = Games.objects.filter(isActive=True)
    shortcode = ''.join(random.sample(letters, 4))

    if "shortcode" in request.POST:
        shortcode = request.POST["shortcode"]
        game, created = Games.objects.get_or_create(shortcode=shortcode)

        msg = "game created" if created else "game already there"

        # "Troll -- in the dungeons -- thought you ought to know."
        messages.success(request, msg)
        return redirect('create')

    return render(request, 'HPHBhelper/index.html',
                  {'shortcode': shortcode, 'active_games': active_games})
