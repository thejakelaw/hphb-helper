from django.db import models
from django import forms

class Games(models.Model):
    shortcode = models.CharField(max_length=4)
    isActive = models.BooleanField(default=False)

    class TurnOrder(models.Model):
        #The turn order is set after a game is created but before it starts
        pass

class Players(models.Model):
    name = models.CharField(max_length=20)
    game = models.ForeignKey(Games,on_delete=models.CASCADE)

    heroes = (
        ("1","Harry Potter"),
        ("2", "Ron Weasley"),
        ("3", "Heromione Granger"),
        ("4", "Ginny Weasley"),
        ("5", "Luna Lovegood")
    )

    player_character = forms.ChoiceField(choices=heroes)
    health = models.IntegerField(default=10)
    coins = models.IntegerField(default=0)
    damage_tokens = models.IntegerField(default=0)
