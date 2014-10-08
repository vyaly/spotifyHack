# shows a user's playlists (need to be authenticated via oauth)
import sys
import os
import spotipy
import spotipy.util as util

# export SPOTIPY_CLIENT_ID='your-spotify-client-id'
# export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
# export SPOTIPY_REDIRECT_URI='your-app-redirect-url'


# export SPOTIPY_CLIENT_ID='44432cf3cd2a4ae2a441fdd45d6dded3'
# export SPOTIPY_CLIENT_SECRET='1da46786036840d68efb174a963dd4e8'
# export SPOTIPY_REDIRECT_URI='http://mysite.com/callback/'


def show_tracks(results):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print "   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name'])


def user_playlists_contents(username):

    token = util.prompt_for_user_token(username, scope=None, client_id = '44432cf3cd2a4ae2a441fdd45d6dded3', client_secret='1da46786036840d68efb174a963dd4e8',redirect_uri='http://localhost:5000/find_list')

    if token:
        top = 40
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print
                print playlist['name']
                print '  total tracks', playlist['tracks']['total']
                results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
                tracks = results['tracks']
                show_tracks(tracks)
                while tracks['next']:
                    tracks = sp.next(tracks)
                    show_tracks(tracks)
    else:
        print "Can't get token for", username

