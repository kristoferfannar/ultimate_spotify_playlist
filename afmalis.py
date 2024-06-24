import json
import requests
from dotenv import load_dotenv, get_key

load_dotenv()

SPOTIFY_TOKEN, SPOTIFY_USER_ID = get_key(".env", "SPOTIFY_TOKEN"), get_key(
    ".env", "SPOTIFY_USER_ID"
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

    if api_response.status_code != 201:
        raise Exception(
            f"failed to create playlist with name {playlistname}: {api_response.text}"
        )

    print(f"created playlist '{playlistname}' with id '{json_response['id']}'")


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
    return response_json["tracks"]["items"][0]


def find_playlist_from_link(playlist_id):
    query = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    header = {
        "Authorization": "Bearer {}".format(SPOTIFY_TOKEN),
        "Content-Type": "application/json",
    }

    playlists_response = requests.get(query, headers=header)

    if playlists_response != 200:
        raise Exception(f"failed to retrieve playlist with id: {playlist_id}")

    json_playlists = playlists_response.json()
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

    if response.status_code != 201:
        raise Exception(
            f"adding songs to playlist with id: {newplaylist_id} failed: {response.text}"
        )


def add_songlist_to_playlist(songlist, playlist_id):
    query = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    # only the first 100 songs can be added per request
    response = requests.post(query, headers=HEADER, data=json.dumps(songlist[:100]))

    if response.status_code != 200:
        raise Exception(
            f"failed to add songs to playlist: status {response.status_code}"
        )

    print(f"added songs: {response}")

    # add the rest of the songs
    if len(songlist) > 100:
        add_songlist_to_playlist(songlist[100:], playlist_id)


def remove_songlist_from_playlist(songlist, playlist_id):
    query = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    # only a 100 songs can be removed per request
    trackdata = {"tracks": [{"uri": i} for i in songlist[:100]]}

    requests.delete(query, headers=HEADER, data=json.dumps(trackdata))

    # remove the other songs
    if len(songlist) > 100:
        remove_songlist_from_playlist(songlist[100:], playlist_id)


def clear_playlist(playlist_id):
    songs = all_songs_from_playlist_id(playlist_id)
    print(f"clearing playlist with {len(songs)} songs...")

    resp = None
    batches = 0
    while len(songs) > 0:
        resp = remove_songlist_from_playlist(songs[: min(len(songs), 100)], playlist_id)
        songs = songs[min(len(songs), 100) :]
        batches += 1
        print(f"batch {batches}")

    if resp is not None:
        print(resp.json())


def print_dict(somedic, indent=""):
    print()
    for key in somedic:
        if isinstance(somedic[key], dict):
            print(indent + key)
            print_dict(somedic[key], indent + "\t")
        else:
            print(indent + key, ":", somedic[key])


if __name__ == "__main__":
    if SPOTIFY_TOKEN is None or SPOTIFY_USER_ID is None:
        raise Exception(".env file not properly configured... Is it missing?")

    playlistname = input("what should your playlist be called? ")
    playlist_descr = input(f"what description will {playlistname} have? ")
    print(f"creating playlist '{playlistname}'...")
    create_playlist(playlistname, playlist_descr)
