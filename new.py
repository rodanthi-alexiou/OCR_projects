import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import json, requests





cid = '6b7f1d575791402cb00578f1fa6bf122'
secret = '28afb5940597469f915e54d37efce4ae'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
spotify_token= "BQCkJMiJxVM4EkGSelHJA5zXlp5g5-hbn2unxq9U5drkcXHSMQ77CRZw1HyQF5WPizcAygmB1Q8osKtM8GkcFrBWCIY6JerQsREkgtRt8iddpslvn_Wg_hIICepvccCEcnbC2VIl2Ls9xhLz4N_k4q07MlxFO8TUJHt9dHhHeTO69u_NArCwHYXUXk-rOMdcckGBdE7VGHRKSP7KuamQyS1foDDv1Y-s9ROii71z7WIzUloesPsWfrC_2zg418n15EGRQSjtg2xDOE7s-iUMjmg"


def getTrackID(name):
    results = sp.search(q='track:' + name, type='track')
    items = results['tracks']['items']
    if not items:
        return 'empty'
    else:
        track = items[0]
        return track['uri']




def add_song_to_playlist():


    song_id=getTrackID("Call Me")
    # create a new playlist
    playlist_id = "0QenuUPQl69LxnVDSOkE6f"
    songs=[]
    songs.append(song_id)
        # add all songs into new playlist
    request_data = json.dumps(songs)

    query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
        playlist_id)

    response = requests.post(
        query,
        data=request_data,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        }
        )


    response_json = response.json()
    return response_json


#print(add_song_to_playlist())