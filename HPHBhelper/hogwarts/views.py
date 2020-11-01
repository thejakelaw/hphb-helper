import random
from string import ascii_uppercase, digits

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import PlayerForm
from .models import Games, Players


def lobby(request):
    # Create Game
    # Join Game
    return HttpResponse("Yer not a wizard yet, 'Arry! Welcome to the Lobby. Check back soon.")


def create_player(request, shortcode):
    form = PlayerForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Added Player')
        return redirect('active-game')
    return render(request, 'HPHBhelper/form.html', {'form': form, 'shortcode': shortcode})


def active_game(request, shortcode):
    game = Games.objects.get(shortcode=shortcode)
    active_players = Players.objects.filter(game=game)
    if active_players:
        return render(request, 'HPHBhelper/game.html', {'shortcode': shortcode, 'active_players': active_players})
    return render(request, 'HPHBhelper/game.html', {'shortcode': shortcode})


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
