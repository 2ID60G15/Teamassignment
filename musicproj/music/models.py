from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=50)
    start_year = models.DateField()
    image = models.FileField(upload_to='artist_img/')
    genre = models.CharField(max_length=100)
    members = models.TextField()


class Album(models.Model):
    name = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist)
    release_date = models.DateTimeField()
    image = models.FileField(upload_to='album_img/')


class Songs(models.Model):
    name = models.CharField(max_length=50)
    album = models.ForeignKey(Album)
    lyrics = models.TextField()


class Torrent(models.Model):
    album = models.ForeignKey(Album)
    magnet = models.CharField(max_length=200)


class UserProfile(models.Model):
    user = models.OneToOneField(User)


class Favorite:
    user = models.ForeignKey(UserProfile)
    album = models.ForeignKey(Album)
