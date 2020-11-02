from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.lobby, name='HPHBhelper'),
    path('new', views.create_game, name='create'),
    path('games/<shortcode>/', views.active_game, name='active-game'),
    path('games/<shortcode>/add/', views.create_player, name='add-player'),
]