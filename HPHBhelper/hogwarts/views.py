from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def lobby(request):
    return HttpResponse("Yer not a wizard yet, 'Arry! Welcome to the Lobby. Check back soon.")
