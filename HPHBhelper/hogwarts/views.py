from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import GameForm
import random


def lobby(request):
    # Create Game

    # Join Game
    # select from list
    return HttpResponse("Yer not a wizard yet, 'Arry! Welcome to the Lobby. Check back soon.")


def create_game(request):
    letters = 'ABCDEFGHJKLMNPQRSTUVWXYZ1234567890'
    shortcode = ''.join((random.choice(letters) for i in range(4)))
    form = GameForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Troll -- in the dungeons -- thought you ought to know.")
        return redirect('hogwarts:HPHBhelper')
    return render(request, 'HPHBhelper/index.html', {'form': form, 'shortcode': shortcode})

