import os

import json
import requests
from dotenv import load_dotenv

load_dotenv()


SPOTIFY_TOKEN, SPOTIFY_USER_ID = os.getenv("SPOTIFY_TOKEN"), os.getenv(
    "SPOTIFY_USER_ID"
)

SITE = "https://open.spotify.com/"
HEADER = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {SPOTIFY_TOKEN}",
}


def create_playlist(
    playlistname, playlistdescription="", publicstatus=False, collabstatus=False
):
    request_body = json.dumps(
        {
            "name": playlistname,
            "description": playlistdescription,
            "public": publicstatus,
            "collaborative": collabstatus,
        }
    )

    endpoint = f"https://api.spotify.com/v1/users/{SPOTIFY_USER_ID}/playlists"
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(SPOTIFY_TOKEN),
    }

    api_response = requests.post(endpoint, data=request_body, headers=header)
    json_response = api_response.json()
    print(api_response)
    print()
    print(json_response)


def get_spotify_uri(songname, artist):
    query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset0&limit=20".format(
        songname, artist
    )

    response = requests.get(
        query,
        headers={
            "Content-type": "application/json",
            "Authorization": "Bearer {}".format(SPOTIFY_TOKEN),
        },
    )
    response_json = response.json()
    # print(response_json)
    # print(response_json)
    return response_json["tracks"]["items"][0]


def find_playlist_from_link(playlist_id):
    query = f"https://api.spotify.com/v1/playlists/{playlist_id}"

    header = {
        "Authorization": "Bearer {}".format(SPOTIFY_TOKEN),
        "Content-Type": "application/json",
    }

    playlists_response = requests.get(query, headers=header)
    json_playlists = playlists_response.json()
    # print(json_playlists)

    return json_playlists


def all_songs_from_playlist_id(playlist_id):
    json_playlist = find_playlist_from_link(playlist_id)
    songslist = [
        i["track"]["uri"] for i in json_playlist["tracks"]["items"]
    ]  # gives me the uris of all the playlist's tracks.

    json_playlist = json_playlist["tracks"]  # to deal with the while loop.
    while (
        json_playlist["next"] is not None
    ):  # if len(sognslist > 100), the json of the response has a 'next' key, containing the rest of the songs.
        json_playlist = requests.get(
            json_playlist["next"],
            headers={
                "Authorization": "Bearer {}".format(SPOTIFY_TOKEN),
                "Content-Type": "application/json",
            },
        )
        json_playlist = json_playlist.json()
        songslist += [i["track"]["uri"] for i in json_playlist["items"]]

    return songslist


def find_id_from_link(
    link,
):  # input a spotify link and outputs the song/playlist id, contained in the link.
    link = link[len(SITE) :]
    slash = link.find("/")
    qm = link.find("?")
    return link[slash + 1 : qm]


def add_from_oldplaylist_to_newplaylist(oldplaylist_link, newplaylist_id):
    oldplaylist_id = find_id_from_link(oldplaylist_link)

    query = f"https://api.spotify.com/v1/playlists/{newplaylist_id}/tracks"
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {SPOTIFY_TOKEN}",
    }

    rdata = all_songs_from_playlist_id(oldplaylist_id)

    response = requests.post(query, headers=header, data=json.dumps(rdata))
    json_resp = response.json()
    # print(json_resp)


def add_songlist_to_playlist(songlist, playlist_id):

    query = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    response = requests.post(query, headers=HEADER, data=json.dumps(songlist[:100]))
    print(response)
    print(response.json())

    if len(songlist) > 100:
        add_songlist_to_playlist(songlist[100:], playlist_id)


def remove_songlist_from_playlist(songlist, playlist_id):
    query = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    trackdata = {"tracks": [{"uri": i} for i in songlist[:100]]}

    response = requests.delete(query, headers=HEADER, data=json.dumps(trackdata))
    print(response)

    if len(songlist) > 100:
        remove_songlist_from_playlist(songlist[100:], playlist_id)


def print_dict(somedic, indent=""):
    print()
    for key in somedic:
        if type(somedic[key]) == dict:
            print(indent + key)
            print_dict(somedic[key], indent + "\t")
        else:
            print(indent + key, ":", somedic[key])


if __name__ == "__main__":
    # create_playlist('Afmælis!', 'Find the bug', False, True) #legacy nuna.!;) #the playlist created for the birthday (containing the 200 most popular songs from Google forms.)
    # create_playlist('Restin', 'Lögin sem komust ekki inn á hinn.', False, True)!;) #a playlist containing the 1100 or so other songs.
    print("creating playlist...")
    create_playlist("new-playlist-to-test")

    pass
