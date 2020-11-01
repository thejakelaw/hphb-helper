from django.db import models
from django import forms

HERO_CHOICES = [
    ("1", "Harry Potter"),
    ("2", "Ron Weasley"),
    ("3", "Heromione Granger"),
    ("4", "Neville Longbottom"),
    ("5", "Luna Lovegood"),
    ("6", "Ginny Weasley")
]
class Games(models.Model):
    shortcode = models.CharField(max_length=4)
    isActive = models.BooleanField(default=True)

    class TurnOrder(models.Model):
        pass
        # The turn order is set after a game is created but before it starts

    def __str__(self):
        return self.shortcode

class Players(models.Model):
    name = models.CharField(max_length=20)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    wizard = forms.ModelChoiceField(queryset=HERO_CHOICES)
    health = models.IntegerField(default=10)
    coins = models.IntegerField(default=0)
    damage_tokens = models.IntegerField(default=0)

    def __str__(self):
        return self.name