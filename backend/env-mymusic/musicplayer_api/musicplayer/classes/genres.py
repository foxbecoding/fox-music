from django.http import Http404
from utils.classes import UniqueId
from musicplayer.models import Genre
from musicplayer.serializers import GenreSerializer, GenreDetailsSerializer

class Create:
    def __init__(self):
        self.uniqid = str(UniqueId())

    def add(self, data: dict) -> list:
        data['uniqid'] = self.uniqid
        serializer = GenreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            message = "Genre created successfully!"
            http_status = 201
            data = {"success_message": message}
            return [data, http_status]
        http_status = 400
        data = {"error_message": serializer.errors}
        return [data, http_status]

class Retrieve:
    def __init__(self):
        self.queryset = ''

    def all(self) -> list:
        self.queryset = Genre.objects.all()
        data = self.__serializer(True)
        http_status = 200
        return [data, http_status]

    def get(self, uniqid: str) -> list:
        try:
            self.queryset = Genre.objects.get(uniqid=uniqid)
            data = self.__serializer(False)
            http_status = 200
            return [data, http_status]
        except:
            raise Http404
        
    def __serializer(self, is_many: bool):
        serializer = GenreDetailsSerializer(self.queryset, many=is_many)
        return serializer.data

class Update(Retrieve):
    def update(self, data: dict, uniqid: str) -> list:
        self.get(uniqid)
        serializer = GenreSerializer(self.queryset, data=data)
        if serializer.is_valid():
            serializer.save()
            data = {"success_message": "Genre updated successfully!"}
            http_status = 200
            return [data, http_status] 
        data = {"error_message": serializer.errors}
        http_status = 400
        return [data, http_status]


class Delete(Retrieve):
    def delete(self, uniqid: str) -> list:
        self.get(uniqid)
        self.queryset.delete()
        data = {"success_message": "Genre deleted successfully"}
        http_status = 200
        return [data, http_status]

    def delete_all(self) -> list:
        self.all()
        self.queryset.delete()
        data = {"success_message": "All genres deleted successfully"}
        http_status = 200
        return [data, http_status]
