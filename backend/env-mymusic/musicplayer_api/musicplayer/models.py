from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, default='', null=True)
    uniqid = models.CharField(max_length=20, default='', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    deleted = models.DateTimeField(null=True)

class Artist(models.Model):
    name = models.CharField(max_length=200, default='', null=True)
    uniqid = models.CharField(max_length=20, default='', null=True)
    img_file_path = models.FileField(upload_to='artist_images/', default='', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    deleted = models.DateTimeField(null=True)

class Song(models.Model):
    genre = models.ForeignKey(
            Genre,
            on_delete=models.SET_DEFAULT,
            related_name='songs',
            default='',
            null=True
    )
    artists = models.ManyToManyField(Artist, related_name='songs')
    title = models.CharField(max_length=200, default='', null=True)
    uniqid = models.CharField(max_length=20, null=True)
    yt_url = models.CharField(max_length=300, default='', null=True)
    thumbnail = models.CharField(max_length=100, default='', null=True)
    filename = models.CharField(max_length=100, default='', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    deleted = models.DateTimeField(null=True)

class Play(models.Model):
    song =  models.ForeignKey(
            Song,
            on_delete=models.CASCADE,
            related_name='plays',
            default='',
            null=True
    )
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    deleted = models.DateTimeField(null=True)


