from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from utils.classes import GetEnv
from musicplayer.classes.songs import Create, Retrieve, Update, Delete

SONGS_FILE_PATH = str(GetEnv("media_root_songs"))
SONG_THUMBNAILS_PATH = str(GetEnv("media_root_song_thumbnails"))

class SongViewSet(viewsets.ViewSet):
    lookup_field = 'uniqid'
    
    def get_permissions(self):
        permission_classes = [IsAdminUser]
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
        
    def list(self, request):
        obj = Retrieve()
        data, http_status = obj.all(request.query_params)
        return Response(data, status=http_status)

    @method_decorator(csrf_protect)
    def create(self, request):
        obj = Create(request.data, SONGS_FILE_PATH, SONG_THUMBNAILS_PATH)
        data, http_status = obj.add()
        return Response(data, status=http_status)

    def retrieve(self, request, uniqid=None):
        obj = Retrieve()
        data, http_status = obj.get(uniqid)
        return Response(data, status=http_status)

    @method_decorator(csrf_protect)
    def update(self, request, uniqid=None):
        obj = Update()
        data, http_status = obj.update(request.data, uniqid)
        return Response(data, http_status)

    @method_decorator(csrf_protect)
    def destroy(self, request, uniqid=None):
        obj = Delete()
        if uniqid != 'all':
            data, http_status = obj.delete(uniqid)
        else:
            data, http_status = obj.delete_all()
        return Response(data, http_status)
