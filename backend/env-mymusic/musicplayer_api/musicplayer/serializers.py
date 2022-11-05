from rest_framework import serializers
from musicplayer.models import Song, Play, Genre, Artist

#Write only serializers
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = [
            'title',
            'uniqid',
            'yt_url',
            'filename',
            'thumbnail',
            'plays',
            'genre',
            'artists'
        ]
        extra_kwargs = {'plays': {'required': False}}

class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ['song']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'uniqid']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'uniqid', 'img_file_path']

#Read only serializers
class SongDetailsSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True, many=False)
    artists = ArtistSerializer(read_only=True, many=True)
    class Meta:
        model = Song
        fields = [
            'title',
            'uniqid',
            'yt_url',
            'filename',
            'thumbnail',
            'plays',
            'genre',
            'artists'
        ]

class PlayDetailsSerializer(serializers.ModelSerializer):
    song = SongDetailsSerializer(read_only=True, many=False)
    class Meta:
        ordering = ['-id']
        model = Play
        fields = ['song']

class GenreDetailsSerializer(serializers.ModelSerializer):
    songs = SongDetailsSerializer(read_only=True, many=True)
    class Meta:
        model = Genre
        fields = ['name', 'uniqid', 'songs']

class ArtistDetailsSerializer(serializers.ModelSerializer):
    songs = SongDetailsSerializer(read_only=True, many=True)
    class Meta:
        model = Artist
        fields = ['name', 'uniqid', 'img_file_path', 'songs']
