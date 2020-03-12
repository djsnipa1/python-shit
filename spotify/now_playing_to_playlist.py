#!/usr/bin/env python3
# coding=utf-8
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env

SPOTIPY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
username = os.getenv("SPOTIFY_USERNAME")

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

scope = 'user-library-read user-read-currently-playing user-read-playback-state user-read-recently-played'
token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

# playlists = sp.user_playlists(username)
# for playlist in playlists['items']:
#     print(playlist['name'])

current_track = sp.current_user_playing_track()


def current_user_playlists():
    current_user_playlists = sp.current_user_playlists()

    while current_user_playlists:
        for i, playlist in enumerate(current_user_playlists['items']):
            print(
                "%4d %s %s" %
                (i +
                 1 +
                 current_user_playlists['offset'],
                 playlist['uri'],
                 playlist['name']))
        if current_user_playlists['next']:
            current_user_playlists = sp.next(current_user_playlists)
        else:
            current_user_playlists = None


current_user = sp.current_user()


def user_playlists():
    playlists = sp.user_playlists(username)

    while playlists:
        for i, playlist in enumerate(playlists['items']):
            print(
                "%4d %s %s" %
                (i +
                 1 +
                 playlists['offset'],
                 playlist['uri'],
                 playlist['name']))
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None


# user_playlists()

print(80 * "-")

print(current_user['display_name'])
print(40 * "=-")
print("Currently Playing...\n")
print("Artist: " + current_track['item']['album']['artists'][0]['name'])
print("Track: " + current_track['item']['name'])
