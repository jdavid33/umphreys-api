import requests
import json


artist_id = '3826a6e0-9ea5-4007-941c-25b9dd943981' #Umphrey's McGee
api_key = 'cBrGLIv4rtdUDI_iV1JRNyvHP_ar8InUWcN9'

# Call Setlist.fm API
url = 'https://api.setlist.fm/rest/1.0/artist/' + artist_id + '/setlists?p=1'
headers = {'Accept': 'application/json', 'x-api-key': api_key}
r = requests.get(url, headers=headers)
	
# Get .json Data
data = r.json()
shows = data['setlist']

def song_was_played(song, date):
    
    # filter setlist data to specified date
    expectedResult = [d for d in shows if d['eventDate'] in date]
    
    # create list of songs played on that date
    songs_played = []
    for x in expectedResult:
        for key, value in x['sets'].items():
            for x in value:
                for x in x['song']:
                    songs_played.append(x['name'])
    
    check = song in songs_played
    return check    