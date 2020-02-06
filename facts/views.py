from django.shortcuts import render
from django.contrib import messages
from django.core.mail import mail_admins
from django.shortcuts import render, redirect
from . import templates

# Create your views here.
from .models import Artist, Song

letters = []
for x in range(1488, 1515):
    if x != 1498 and x != 1503 and x != 1507 and x != 1509 and x != 1501:
        letters.append(chr(x))


def home(request):
    context = {'letters': letters}
    return render(request, 'facts/home_page.html', context)


def artists(request, let):
    artist_list = []
    for artist in Artist.objects.all():
        if artist.name:
            if artist.name[0] == let:
                artist_list.append(artist.name)
    context = {
        'let': let,
        'count': len(artist_list),
        'letters': letters,
        'artist_list': artist_list
    }
    return render(request, 'facts/artists.html', context)


def songs(request, let):
    songs_list = []
    for song in Song.objects.all():
        if song.name:
            if song.name[0] == let:
                songs_list.append(song.name)
    context = {
        'let': let,
        'count': len(songs_list),
        'letters': letters,
        'artist_list': songs_list
    }
    return render(request, 'facts/song.html', context)