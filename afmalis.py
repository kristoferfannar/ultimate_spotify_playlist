import json
import requests
from secretsAPI import spotify_token, spotify_user_id, python_playlist_id
SITE = 'https://open.spotify.com/'

CLIENTID = 'c79f8f3e44374b02a328880197d78508'
CLIENTSECRET = '4223f8c46a6f418f97c2d7886c253793' # frá appinu í spotify for develepors
playlist = 'https://open.spotify.com/playlist/3MDQyYbnII6FS2k81Jmgn9?si=3d03e1bba6fd4a2f' # Útileguplaylistinn minn
HEADER = {'Content-Type':'application/json','Authorization': f'Bearer {spotify_token}'}



def create_playlist(playlistname, playlistdescription = '', publicstatus = False):
    request_body = json.dumps({
        "name": playlistname,
        "description": playlistdescription,
        "public": publicstatus
        })

    endpoint = f"https://api.spotify.com/v1/users/{spotify_user_id}/playlists"
    header = {'Content-Type':'application/json', 'Authorization':'Bearer {}'.format(spotify_token)}


    api_response = requests.post(endpoint, data = request_body, headers = header)
    json_response = api_response.json() 
    print(api_response)
    print()
    print(json_response)





def get_spotify_uri(songname, artist):
    query = 'https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset0&limit=20'.format(songname, artist)

    response = requests.get(query, headers={"Content-type": "application/json", "Authorization": "Bearer {}".format(spotify_token)})
    response_json = response.json()
    #print(response_json)
    #print(response_json)
    return response_json["tracks"]["items"][0]



def find_playlist_from_link(playlist_id):

    query = f'https://api.spotify.com/v1/playlists/{playlist_id}'

    header = {'Authorization': 'Bearer {}'.format(spotify_token), 'Content-Type':'application/json'}

    playlists_response = requests.get(query, headers = header)
    json_playlists = playlists_response.json()
    #print(json_playlists)

    return json_playlists

def all_songs_from_playlist_id(playlist_id): #have to deal with if len(songslist > 100)
    json_playlist = find_playlist_from_link(playlist_id)
    songslist = [i['track']['uri'] for i in json_playlist['tracks']['items']] #gives me the uris of all the playlist's tracks.
    
    json_playlist = json_playlist['tracks'] #to deal with the while loop.
    while json_playlist['next'] is not None:
        json_playlist = requests.get(json_playlist['next'], headers = {'Authorization': 'Bearer {}'.format(spotify_token), 'Content-Type':'application/json'})
        json_playlist = json_playlist.json()
        songslist += [i['track']['uri'] for i in json_playlist['items']]
    
    return songslist

def find_id_from_link(link):
    link = link[len(SITE):]
    slash = link.find('/')
    qm = link.find('?')
    return link[slash+1:qm]


def add_from_oldplaylist_to_newplaylist(oldplaylist_link, newplaylist_id):
    oldplaylist_id = find_id_from_link(oldplaylist_link)

    query = f'https://api.spotify.com/v1/playlists/{newplaylist_id}/tracks'
    header = {'Content-Type':'application/json','Authorization': f'Bearer {spotify_token}'}

    rdata = all_songs_from_playlist_id(oldplaylist_id)

    response = requests.post(query, headers= header, data=json.dumps(rdata))
    json_resp = response.json()
    #print(json_resp)


def add_songlist_to_playlist(songlist, playlist_id):

    query = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    response = requests.post(query, headers = HEADER, data = json.dumps(songlist[:100]))
    print(response)
    
    if len(songlist) > 100:
        add_songlist_to_playlist(songlist[100:], playlist_id)


def remove_songlist_from_playlist(songlist, playlist_id):
    query = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    trackdata = {"tracks":[{"uri":i} for i in songlist[:100]]}

    response = requests.delete(query, headers = HEADER, data = json.dumps(trackdata))
    print(response)

    if len(songlist) > 100:
        remove_songlist_from_playlist(songlist[100:], playlist_id)


def print_dict(somedic, indent = ''):
    print()
    for key in somedic:
        if type(somedic[key]) == dict:
            print(indent + key)
            print_dict(somedic[key], indent + '\t')
        else:
            print(indent + key,':', somedic[key])



if __name__ == "__main__":

    #create_playlist('Python2', 'önnur tilraun', True)
    
    pass