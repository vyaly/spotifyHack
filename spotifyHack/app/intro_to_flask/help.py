import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'
SPOTIPY_CLIENT_ID='44432cf3cd2a4ae2a441fdd45d6dded3'
SPOTIPY_CLIENT_SECRET='1da46786036840d68efb174a963dd4e8'
SPOTIPY_REDIRECT_URI='http://mysite.com/callback/'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, scope,SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)


if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print track['name'] + ' - ' + track['artists'][0]['name']
else:
    print "Can't get token for", username