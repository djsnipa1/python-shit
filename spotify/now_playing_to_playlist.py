#!/usr/bin/env python3
# coding=utf-8
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
from dotenv import load_dotenv
import os

# import sys


# if len(sys.argv) > 3:
#     username = sys.argv[1]
#     playlist_id = sys.argv[2]
#     track_ids = sys.argv[3:]
# else:
#     print("Usage: %s username playlist_id track_id ..." % (sys.argv[0],))
#     sys.exit()

load_dotenv()  # loads .env

SPOTIPY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
username = os.getenv("SPOTIFY_USERNAME")

client_credentials_manager = SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

scope = "playlist-modify-private user-library-read " \
        "user-read-currently-playing user-read-playback-state " \
        "user-read-recently-played"
token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID,
                                   SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

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

print(80 * "-")  # Displays -----
print(current_user['display_name'])  # Displays user's real name
print(40 * "=-")  # displays -=-=-=-=-

current_track_artist_name = current_track['item']['artists'][0]['name']
current_track_name = current_track['item']['name']

try:
    print("Currently Playing...\n")
    print("Artist: " + current_track_artist_name)
    print("Track: " + current_track_name)
except TypeError:
    print("Nothing is currently playing")

playlist_id = "4LX0m5XMIUVpiktVfUu1qY"


def current_track_to_playlist():
    """
    Adds currently playing track to playlist
    """
    # spotify:playlist:4LX0m5XMIUVpiktVfUu1qY
    tracks = [current_track['item']['id']]
    # pprint(current_track['item'])
    added_to_playlist = sp.user_playlist_add_tracks(
        username, playlist_id, tracks)
    print(added_to_playlist)


def print_playlist_tracks():
    """
    This prints a list of tracks in a playlist.
    'track' , 'id' , 'name'
    """
    offset = 0
    while True:
        response = sp.playlist_tracks(playlist_id,
                                      offset=offset,
                                      fields='items.track.name,'
                                             'items.track.id,total')
        pprint(response['items'])
        offset = offset + len(response['items'])
        print(offset, "/", response['total'])

        if len(response['items']) == 0:
            break


print("Do you want to add '" + current_track_artist_name +
      " = " + current_track_name + "' to a playlist?")
playlist_choice = str.lower(input("[Y]es or [N]o ? "))
# number2 = float(input("Enter the second number: "))
# solution = number1 + number2
# print("The sum of your numbers is {}".format(solution))
if playlist_choice == "y":
    current_track_to_playlist()
    print_playlist_tracks()
else:
    print_playlist_tracks()
