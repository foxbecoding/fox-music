from musicplayer.models import Play
from musicplayer.classes.songs import Retrieve as Retrieve_Songs
from musicplayer.serializers import PlaySerializer, PlayDetailsSerializer

class Create:
    def add(self, data: dict) -> list:
        song_obj = Retrieve_Songs()
        song_obj.get(data['song'])
        data['song'] = song_obj.queryset.pk
        serializer = PlaySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {"success_message": "Song played."}
            http_status = 201
            return [data, http_status]
        data = {"error_message": serializer.errors}
        http_status = 400
        return [data, http_status]

class Retrieve:
    def all(self) -> list:
        queryset = Play.objects.all()
        serializer = PlayDetailsSerializer(queryset, many=True)
        data = serializer.data
        http_status = 200
        return [data, http_status]
