from django.urls import path

from . import views

app_name = "facts"

urlpatterns = [
    path('', views.home, name="home"),
    path('artist/<str:let>', views.artists, name="home"),
    path('song/<str:let>', views.songs, name="home"),
    path('song_artist/<str:name>', views.songs_by_artist, name="home"),
    path('facts/<str:song>/<str:artist>', views.facts, name="home"),
    path('search', views.search, name="home"),
    ]