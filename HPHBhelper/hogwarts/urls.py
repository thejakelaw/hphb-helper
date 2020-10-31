from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.lobby, name='HPHBhelper'),
    path('new', views.create_game, name='create'),
    re_path(r'^hogwarts/games/(?P<shortcode>[A-Z0-9]{4})$', views.active_game, name='active-game')
]