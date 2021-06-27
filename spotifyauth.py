import spotipy
from spotipy.oauth2 import SpotifyOAuth,SpotifyClientCredentials


scope = "user-library-read"
cid = '6b7f1d575791402cb00578f1fa6bf122'
secret = '28afb5940597469f915e54d37efce4ae'
red_uri="https://www.spotify.com/gr/home/"
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager,auth_manager=SpotifyOAuth(client_id=cid,client_secret=secret,redirect_uri=red_uri))


results = sp.current_user_saved_tracks()
#for idx, item in enumerate(results['items']):
#    track = item['track']
#    print(idx, track['artists'][0]['name'], " – ", track['name'])