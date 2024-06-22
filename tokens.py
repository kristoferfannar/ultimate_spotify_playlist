# Creates an access token using the spotify API:
# https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token
from dotenv import load_dotenv, set_key, get_key
import requests
import subprocess

load_dotenv()

CLIENT_ID = get_key(".env", "CLIENT_ID")
CLIENT_SECRET = get_key(".env", "CLIENT_SECRET")
uri_decrypt = "https%3A%2F%2Fgoogle.com"

spotify_auth_uri = "https://accounts.spotify.com/authorize?client_id={}&response_type=code&redirect_uri={}&scope=playlist-modify-public%20playlist-modify-private".format(
    CLIENT_ID, uri_decrypt
)  # skoða scope fyrir private playlista??
print(spotify_auth_uri)


def get_access_token():
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    response = requests.post(
        "https://accounts.spotify.com/api/token", headers=headers, data=data
    )
    json_response = response.json()

    return json_response["access_token"]


if __name__ == "__main__":
    # allow this client (this program) to have access to my spotify account.
    # This is only required once
    subprocess.run(f"open '{spotify_auth_uri}'", shell=True)

    access_token = get_access_token()
    set_key(".env", "SPOTIFY_TOKEN", access_token)
    print("new access token set")
