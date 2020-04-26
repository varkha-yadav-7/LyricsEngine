import requests
import json

API_KEY='103db3d4381270087a1090c46a745485'
url='https://api.musixmatch.com/ws/1.1/'

def searchArtist(artist):
	method='artist.search'
	payload={'artist':artist,'apikey':API_KEY,'page_size':10}
	r=requests.get(url+method,params=payload)
	data=r.json()
	dict=data['message']['body']['artist_list']
	return dict

def searchAlbums(artist_id):
	method='artist.albums.get'
	payload={'artist_id':artist_id,'apikey':API_KEY,'g_album_name':1}
	r=requests.get(url+method,params=payload)
	data=r.json()
	dict=data['message']['body']['album_list']
	return dict

def getAlbumTrack(album_id):
	method='album.tracks.get?'
	payload={'album_id':album_id,'apikey':API_KEY,'page_size':10}
	r=requests.get(url+method,params=payload)
	data=r.json()
	dict=data['message']['body']['track_list']
	return dict

def searchTopTracks(artist):
	method='track.search'
	payload={'q_artist':artist,'apikey':API_KEY,'page_size':10}
	r=requests.get((url+method),params=payload)
	data=r.json()
	if(data['message']['header']['status_code']==404):
		return "No such track found"
	dict=data['message']['body']['track_list']
	return dict

def searchTrack(track,artist):
	method='matcher.track.get?'
	payload= {'q_artist':artist,'q_track':track,'f_has_lyrics':1,'apikey':API_KEY}
	r=requests.get((url+method),params=payload)
	data=r.json()
	if(data['message']['header']['status_code']==404):
		return "No such Track Found"
	dict={'track_id':data['message']['body']['track']['track_id'],'track_name':data['message']['body']['track']['track_name'],'album_name':data['message']['body']['track']['album_name'],'artist_name':artist}
	return dict

def getLyrics(track_id):
	method='track.lyrics.get?'
	payload= {'track_id':track_id,'apikey':API_KEY}
	r=requests.get((url+method),params=payload)
	data=r.json()
	if(data['message']['header']['status_code']==404):
		return "We're sorry ....No such Lyrics found"
	dict=data['message']['body']['lyrics']['lyrics_body']
	return dict

