import os
import urllib.request
from pytube import YouTube
from django.http import Http404
from utils.classes import UniqueId
from musicplayer.models import Song, Genre, Artist
from musicplayer.serializers import SongSerializer, SongDetailsSerializer


class Create:
    def __init__(self, data: dict, file_path: str, thumbnail_path: str):
        self.yt_data = {}
        self.data = data
        self.uniqid = str(UniqueId())
        self.file_path = file_path
        self.thumbnail_path = thumbnail_path
        self.out_file = ''

    def add(self) -> list:
        self.__get_youtube_data()
        self.__get_thumbnail()
        self.__download_mp3_file()
        self.__rename_mp3_file()
        self.__set_song_data()
        return self.__save()

    def __get_youtube_data(self) -> None:
        self.yt_data = YouTube(self.data['yt_url'])

    def __get_thumbnail(self) -> None:
        full_thumbnail_path = self.thumbnail_path+self.uniqid+'.jpg'
        urllib.request.urlretrieve(self.yt_data.thumbnail_url, full_thumbnail_path)

    def __download_mp3_file(self) -> None:
        mp3 = self.yt_data.streams.filter(only_audio=True).first()
        self.out_file = mp3.download(output_path=self.file_path, filename=self.uniqid)

    def __rename_mp3_file(self) -> None:
        base, ext = os.path.splitext(self.out_file)
        new_file = base + ".mp3"
        os.rename(self.out_file, new_file)

    def __set_song_data(self) -> None:
        self.data['uniqid'] = self.uniqid
        self.data['filename'] = self.uniqid+'.mp3'
        self.data['thumbnail'] = self.uniqid+'.jpg'
        self.data['genre'] = Genre.objects.get(uniqid=self.data['genre']).pk
        self.data['artists'] = Artist.objects.values_list('pk', flat=True).filter(uniqid__in=self.data['artists'])

    def __save(self) -> list: 
        serializer = SongSerializer(data=self.data)
        if serializer.is_valid():
            serializer.save()
            data = {"success_message": "Song added successfully!"}
            http_status = 201
            return [data, http_status]
        data = {"error_message": serializer.errors}
        http_status = 400
        return [data, http_status]

class Retrieve:
    def __init__(self):
        self.queryset = ''

    def get(self, uniqid: str) -> list:
        try:
            self.queryset = Song.objects.get(uniqid=uniqid)
            data = self.__serialize(False)
            http_status = 200
            return [data, http_status]
        except Song.DoesNotExist:
            raise Http404

    def all(self, query: dict) -> list:
        limit: int = None
        if 'limit' in query: limit = int(query['limit'])
        self.queryset = Song.objects.all()
        data = self.__serialize(True)[0:limit]
        http_status = 200
        return [data, http_status]

    def __serialize(self, is_many: bool):
        serializer = SongDetailsSerializer(self.queryset, many=is_many)
        return serializer.data

class Update(Retrieve):
    def update(self, data: dict, uniqid: str) -> list:
        self.get(uniqid)
        data['genre'] = Genre.objects.get(uniqid=data['genre']).pk
        data['artists'] = Artist.objects.values_list('pk', flat=True).filter(uniqid__in=data['artists'])
        serializer = SongSerializer(self.queryset, data=data)
        if serializer.is_valid():
            serializer.save()
            data = {"success_message": "Song updated successfully!"}
            http_status = 200
            return [data, http_status]
        data = {"error_message": serializer.errors}
        http_status = 400
        return [data, http_status]

class Delete(Retrieve):
    def delete(self, uniqid: str) -> list:
        self.get(uniqid)
        self.queryset.delete()
        data = {"success_message": "Song deleted successfully!"}
        http_status = 200
        return [data, http_status]

    def delete_all(self) -> list:
        self.all()
        self.queryset.delete()
        data = {"success_message": "All songs deleted successfully!"}
        http_status = 200
        return [data, http_status] 
