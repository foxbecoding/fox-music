from rest_framework.routers import DefaultRouter
from musicplayer.views import song_views, play_views, genre_views, artist_views

router = DefaultRouter()
router.register(r'genres', genre_views.GenreViewSet, basename='genre')
router.register(r'artists', artist_views.ArtistViewSet, basename='artist')
router.register(r'songs', song_views.SongViewSet, basename='song')
router.register(r'plays', play_views.PlayViewSet, basename='play')
urlpatterns = router.urls
