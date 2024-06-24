# Creates an access token using the spotify API:
# https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token
from dotenv import load_dotenv, set_key, get_key
import requests
from time import sleep
import webbrowser

load_dotenv()

CLIENT_ID = get_key(".env", "CLIENT_ID")
CLIENT_SECRET = get_key(".env", "CLIENT_SECRET")
uri_decrypt = "https%3A%2F%2Fgoogle.com"

spotify_auth_uri = "https://accounts.spotify.com/authorize?client_id={}&response_type=code&redirect_uri={}&scope=playlist-modify-public%20playlist-modify-private".format(
    CLIENT_ID, uri_decrypt
)


def get_access_token(code):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "https://google.com",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    response = requests.post(
        "https://accounts.spotify.com/api/token", headers=headers, data=data
    )
    if response.status_code != 200:
        raise Exception("failed to create token: ", response.text)

    json_response = response.json()

    return json_response["access_token"]


if __name__ == "__main__":
    print("This script creates an access token for you...")
    sleep(1.5)
    print(
        """
When you're ready, your browser will be opened with a link to a page asking for permissions to get access to your account...
When you accept, you'll be redirected to google.com.
If you've already given permissions to this program, you'll be redirected to google.com right away."""
    )
    sleep(3.5)
    print(
        """
When at google.com, you'll find a token in the `code` URL query parameter. Something like this:
https://google.com?code=<this-token>"""
    )
    sleep(2.5)
    print(
        """
Copy it and paste it here once you're ready!
This token will be saved in your .env file and will allow you to use the other scripts provided in this repo!
"""
    )
    input("press ENTER to open the link...")
    webbrowser.open(spotify_auth_uri)

    code = input("code: ")

    resp = requests.get(spotify_auth_uri)
    print(resp)
    access_token = get_access_token(code)
    set_key(".env", "SPOTIFY_TOKEN", access_token)
    print("new access token set")
