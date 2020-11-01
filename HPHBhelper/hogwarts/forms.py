from django.forms import ModelForm

from .models import Players

class PlayerForm(ModelForm):
    class Meta:
        model = Players
        fields = ['name', 'wizard']