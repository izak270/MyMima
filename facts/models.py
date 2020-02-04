import datetime

from django.db import models
from django.utils import timezone


class Artist(models.Model):
    artist_first_name = models.CharField(max_length=200)
    artist_last_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.artist_first_name, self.artist_last_name


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Facts(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    fact = models.TextField()
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')