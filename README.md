# ultimate_spotify_playlist

trying to create the absolute best spotify playlist, using Spotify's API.

Plan:
Creating a playlist for a birthday party, with all the best songs according to birthday guests.
Birthday guests send their spotify playlist as a link through google forms.
I download a csv file from google forms (Playlistar/Lög.csv) with all the playlist information.
I collect all the songs in all the playlists, including which songs are most popular (in most playlists). (foldercalc.py)
From that info, I create a playlist of my own with Spotify's API, to create a playlist with all the songs in the birthday guests' playlist. (afmalis.py)
Everyone wins.

## Setting up

1.

```
pip install -r requirements.txt
```

2.

Create a Spotify Developer Project dashboard at https://developer.spotify.com/dashboard
Copy the Client ID and Client Secret into a `.env` file in this directory.

3.

Allow your Project to gain access to some scopes within your account by running:

```bash
python tokens.py
```

This will also create an access token, which will be placed in your `.env`.
It only lasts an hour, so make sure to periodically execute this program periodically.

4.

To grab songs into a csv from playlist links, run:

```bash
# requires SPOTIFY API TOKEN
python foldercalc.py
```

To sort through the song csv and find the most popular songs, run:

```bash
python operations.py
```

To create a new playlist with the calculations, run:

```bash
# requires SPOTIFY API TOKEN
python afmalis.py
```
