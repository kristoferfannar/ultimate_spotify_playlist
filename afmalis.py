import json
import requests
from secretsAPI import spotify_token, spotify_user_id
import pprint
printer = pprint.PrettyPrinter()

CLIENTID = 'c79f8f3e44374b02a328880197d78508'
CLIENTSECRET = '4223f8c46a6f418f97c2d7886c253793' # frá appinu í spotify for develepors
playlist = 'https://open.spotify.com/playlist/3MDQyYbnII6FS2k81Jmgn9?si=3d03e1bba6fd4a2f' # Útileguplaylistinn minn



def create_playlist():
    request_body = json.dumps({
        "name": "PythonPrufa",
        "description": "Fyrsti python playlistinn",
        "public": False
        })

    endpoint = f"https://api.spotify.com/v1/users/{spotify_user_id}/playlists"
    header = {'Content-Type':'application/json', 'Authorization':'Bearer {}'.format(spotify_token)}


    api_response = requests.post(endpoint, data = request_body, headers = header)
    json_response = api_response.json() 
    print(json_response)

# def find_playlist(playlistid):

#     endpoint = 'https://api.spotify.com/v1/playlists/{playlist_id}'.format(playlist_id = playlistid)

#     header = {'Authorization': 'Bearer {token}'.format(CLIENTSECRET), 'Content-Type':'application/json'}

#     playlists_response = requests.get(endpoint, headers = header)
#     json_playlists = playlists_response.json()
#     print(json_playlists)




def get_spotify_uri(songname, artist):
    query = 'https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset0&limit=20'.format(songname, artist)

    response = requests.get(query, headers={"Content-type": "application/json", "Authorization": "Bearer {}".format(spotify_token)})
    response_json = response.json()
    #print(response_json)
    #print(response_json)
    return response_json["tracks"]["items"][0]


response_json = get_spotify_uri("ballin", "logic")

response_list = response_json

#print(response_list.keys())
response_list["album"].pop("available_markets")
for item in ["available_markets", "duration_ms", "disc_number", "explicit", "track_number"]:
    response_list.pop(item)


def find_playlist_from_link(playlistlink):
    pass




def print_dict(somedic, indent = ''):
    print()
    for key in somedic:
        if type(somedic[key]) == dict:
            print(indent + key)
            print_dict(somedic[key], indent + '\t')
        else:
            print(indent + key,':', somedic[key])

#print_dict(response_list)

create_playlist()