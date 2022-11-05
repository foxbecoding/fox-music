from django.http import Http404
from utils.classes import UniqueId
from musicplayer.models import Artist
from musicplayer.serializers import ArtistSerializer, ArtistDetailsSerializer

class Create:
    def __init__(self):
        self.uniqid = str(UniqueId())

    def add(self, data: dict) -> list:
        data['uniqid'] = self.uniqid
        serializer = ArtistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {"success_message": "Artist created successfully!"}
            http_status = 201
            return [data, http_status]
        data = {"error_message": serializer.errors}
        http_status = 400
        return [data, http_status]

class Retrieve:
    def __init__(self):
        self.queryset = ''

    def all(self, query: dict) -> list:
        limit: int = None
        if 'limit' in query: limit = int(query['limit'])
        self.queryset = Artist.objects.all()
        data = self.__serializer(True)[0:limit]
        http_status = 200
        return [data, http_status]

    def get(self, uniqid: str) -> list:
        try:
            self.queryset = Artist.objects.get(uniqid=uniqid)
            data = self.__serializer(False)
            http_status = 200
            return [data, http_status]
        except:
            raise Http404

    def __serializer(self, is_many):
        serializer = ArtistDetailsSerializer(self.queryset, many=is_many)
        return serializer.data

class Update(Retrieve):
    def update(self, data: dict, uniqid: str) -> list:
        self.get(uniqid)
        serializer = ArtistSerializer(self.queryset, data=data)
        if serializer.is_valid():
            serializer.save()
            data = {"success_message": "Artist updated successfully!"}
            http_status = 200
            return [data, http_status] 
        data = {"error_message": serializer.errors}
        http_status = 400
        return [data, http_status]
  
class Delete(Retrieve):
    def delete(self, uniqid: str) -> list:
        self.get(uniqid)
        self.queryset.delete()
        data = {"success_message": "Artist deleted successfully"}
        http_status = 200
        return [data, http_status]

    def delete_all(self) -> list:
        self.all()
        self.queryset.delete()
        data = {"success_message": "All artists deleted successfully"}
        http_status = 200
        return [data, http_status]
