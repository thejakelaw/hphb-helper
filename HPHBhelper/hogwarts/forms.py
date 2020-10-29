from django.forms import ModelForm

from .models import Games

class GameForm(ModelForm):
    class Meta:
        model = Games
        fields = ['shortcode']