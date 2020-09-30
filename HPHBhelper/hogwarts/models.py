from django.db import models

# Create your models here.
class Games(models.Model):
    shortcode = models.CharField(max_length=4)
    isActive = models.BooleanField(default=False)
    host = models.ForeignKey(Players)

    class TurnOrder(models.Model):
        #The turn order is set after a game is created but before it starts
        pass


class Players(models.Model):
    name = models.CharField(max_length=20)
    game = models.ForeignKey(Games)

    class Characters(models.IntegerChoices):
        HARRY_POTTER = 1
        RON_WEASLEY = 2
        HERMIONE_GRANGER = 3
        GINNY_WEASLEY = 4
        LUNA_LOVEGOOD = 5

    player_character = models.IntegerField(choices=Characters.choices)
    health = models.IntegerField(default=10)
    coins = models.IntegerField(default=0)
    damage_tokens = models.IntegerField(default=0)

class Villians(models.Model):
    name = models.CharField(max_length=50)
    health = models.IntegerField(default=0)
    bonus_health = models.IntegerField(default=0) #bonus_* happens when defeated
    bonus_coins = models.IntegerField(default=0)
    bonus_control = models.IntegerField(default=0)
    bonus_draw = models.IntegerField(default=0)
    abilities = models.IntegerField(max_length=500) #maybe this can be broken down more?
