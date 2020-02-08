from django.shortcuts import render
from django.contrib import messages
from django.core.mail import mail_admins
from django.shortcuts import render, redirect
from . import templates

# Create your views here.
# from .forms import Search
from .models import Artist, Song, Facts

letters = []
for x in range(1488, 1515):
    if x != 1498 and x != 1503 and x != 1507 and x != 1509 and x != 1501:
        letters.append(chr(x))


def home(request):
    # form = Search()
    context = {'letters': letters,
               # 'form': form
               }
    return render(request, 'facts/home_page.html', context)


def artists(request, let):
    artist_list = []
    for artist in Artist.objects.order_by('name'):
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
    for song in Song.objects.order_by('name'):
        if song.name:
            if song.name[0] == let:
                songs_list.append((song.name, song.artist.name))
    context = {
        'let': let,
        'count': len(songs_list),
        'letters': letters,
        'artist_list': songs_list
    }
    return render(request, 'facts/song.html', context)


def songs_by_artist(request, name):
    songs = []
    for song in Song.objects.order_by('name'):
        if song.artist.name == name:
            songs.append((song.name, name))
    context = {'songs': songs, 'letters': letters, 'count': len(songs), 'name': name}
    return render(request, 'facts/songs_by_artist.html', context)


def facts(request, song, artist):
    facts = []
    colors = ['#CCFFCC', '#EDF3FE']
    print(len(song))
    i = 0
    for fact in Facts.objects.all():
        if fact.song.name == song:
            facts.append((fact.fact, colors[i % 2]))
            i += 1
    context = {'facts': facts,
               'artist': artist,
               'letters': letters,
               'name': song
               }
    return render(request, 'facts/facts.html', context)


def search(request):
    colors = ['#CCFFCC', '#EDF3FE']
    query = request.GET.get('q')
    artist_results = Artist.objects.filter(name__contains=query)
    song_results = Song.objects.filter(name__contains=query)
    search_fact = Facts.objects.filter(fact__contains=query)
    i = 0
    fact_results = []
    for fact in search_fact:
        fact_results.append((fact, colors[i % 2]))
        i += 1
    context = {
        "artist_results": artist_results,
        "song_results": song_results,
        "fact_results": fact_results,
        'letters': letters,
        'colors': colors
    }
    return render(request, 'facts/search.html', context)
