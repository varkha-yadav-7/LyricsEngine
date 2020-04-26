from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('searchArtist/',views.searchArtist),
    path('searchSpecificSong/',views.searchSpecificSong),
    path('searchArtist/searchAlbum/',views.searchAlbum),
    path('searchArtist/searchAlbum/tracks/',views.tracks),
    path('searchArtist/searchAlbum/tracks/lyrics/',views.lyrics),
    path('searchTopTracks/',views.searchTopTracks),
    path('searchTopTracks/lyrics/',views.lyrics),
]