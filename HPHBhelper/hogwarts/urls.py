from django.urls import path

from . import views

urlpatterns = [
    path('', views.lobby, name='HPHBhelper'),
    path('new', views.create_game, name='create'),
]