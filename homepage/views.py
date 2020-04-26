from django.shortcuts import render
from . import myapi

def homepage(request):
    return render(request,'homepage.html',context=None)

def searchSpecificSong(request):
    track=request.POST.get('song')
    artist=request.POST.get('artist')
    song={}
    song['i']=myapi.searchTrack(track,artist)
    if(song['i']=='No such Track Found'):
        return render(request,'result.html',song)
    track_id=song['i']['track_id']
    song['j']=myapi.getLyrics(track_id)
    return render(request,'searchSpecific.html',song)

def searchArtist(request):
    artist=request.POST.get('artist')
    myartist=myapi.searchArtist(artist)
    return render(request,'artists.html',{'artist':myartist})

def searchAlbum(request):
    artist_id=request.POST.get('artist_id')
    j=""
    album=myapi.searchAlbums(artist_id)
    if(album==[]):
        j="No Album found"
    print(album)
    return render(request,'albums.html',{'albums':album,'j':j})

def tracks(request):
    album_id=request.POST.get('album_id')
    track=myapi.getAlbumTrack(album_id)
    j=""
    if(track==[]):
        j="No Track found"
    return render(request,'tracks.html',{'tracks':track,'j':j})

def lyrics(request):
    track_id=request.POST.get('track_id')
    ly={}
    lyric=myapi.getLyrics(track_id)
    ly['i']=lyric
    return render(request,'result.html',ly)

def searchTopTracks(request):
    artist=request.POST.get('artist')
    tracks=myapi.searchTopTracks(artist)
    return render(request,'tracks.html',{'tracks':tracks})
