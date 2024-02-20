import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyController():
    def __init__(self, client_id, client_secret, redirect_uri, playlist_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.playlist_uri = playlist_uri

    def authenticator(self):
        spotify = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=self.client_id,
                client_secret=self.client_secret,
                redirect_uri=self.redirect_uri,
                scope="user-read-playback-state,user-modify-playback-state"
            )
        )
        return spotify
    
    def play_tracks(self, spotify):
        audios_uri = self.select_tracks(spotify)
        spotify.start_playback(uris=audios_uri)

    def pause(self, spotify):
        spotify.pause_playback()

    def resume(self, spotify):
        spotify.start_playback()
        
    def select_tracks(self, spotify):
        playlist_id = self.playlist_uri.split(':')[-1]
        playlist_tracks = spotify.playlist_tracks(playlist_id)
        audios_uri = [track['track']['uri'] for track in playlist_tracks['items']]
        return audios_uri
    

