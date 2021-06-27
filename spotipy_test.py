import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import json




cid = '6b7f1d575791402cb00578f1fa6bf122'
secret = '28afb5940597469f915e54d37efce4ae'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def getTrackID(name):
    results = sp.search(q='track:' + name, type='track')
    items = results['tracks']['items']
    if not items:
        return 'empty'
    else:
        track = items[0]
        print(items[1]['name'])
        print(items[2]['name'])
        return track['uri']

user_id = "11170000573"
playlist_id = "0QenuUPQl69LxnVDSOkE6f"
print(sp.current_user)
song_id=getTrackID("Call Me")
#sp.user_playlist_add_tracks(user_id, playlist_id, song_id, position=None)

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Radiohead'

results = sp.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])
    print(artist['uri'])
    top=[]
    top = sp.artist_top_tracks(artist['uri'],'US')
    for i in top['tracks']:
        print(i['name'] + ' : ' + i['uri'])


