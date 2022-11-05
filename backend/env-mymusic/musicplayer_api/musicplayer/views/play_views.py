from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from musicplayer.classes.plays import Create, Retrieve


class PlayViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    lookup_field = 'uniqid'
    def list(self, request):
        obj = Retrieve()
        data, http_status = obj.all()
        return Response(data, status=http_status)

    def create(self, request):
        obj = Create()
        data, http_status = obj.add(request.data)
        return Response(data, status=http_status)
