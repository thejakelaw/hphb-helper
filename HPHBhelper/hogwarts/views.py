import random
from string import ascii_uppercase, digits

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import GameForm
from .models import Games


def lobby(request):
    # Create Game

    # Join Game
    # select from list
    return HttpResponse("Yer not a wizard yet, 'Arry! Welcome to the Lobby. Check back soon.")


def create_game(request):
    letters = 'ABCDEFGHJKLMNPQRSTUVWXYZ1234567890'
    # letters = ascii_uppercase + digits

    shortcode = ''.join(random.sample(letters, 4))

    if "shortcode" in request.POST:
        shortcode = request.POST["shortcode"]
        game, created = Games.objects.get_or_create(shortcode=shortcode)

        msg = "game created" if created else "game already there"

        # "Troll -- in the dungeons -- thought you ought to know."
        messages.success(request, msg)
        return redirect('create')

    return render(request, 'HPHBhelper/index.html',
                  {'shortcode': shortcode})
