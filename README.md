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

## Background

This repository was originally created when I had just started learning programming, and was my first real personal project.
I was about to throw a birthday party, and wanted to create the absolute best playlist for the party.

I had noticed a trend with recent events, hosts created a public spotify playlist for guests to add their favourite songs to.
While the idea was good, it's fun to create a group playlist with everyone's favourite song, the execution wasn't that great.
Adding songs individually, one-by-one, was a hassle, and people could see who was adding each song, which felt awkward if only one or two people seemed overly excited about adding songs, while other didn't participate as much.

I thought to myself that this idea could be executed better, and created a Google Forms document for people to submit links to their favourite Spotify playlists, shortly explaining to them that I had a script create a single playlist with the most popular (most occurring) songs.

I had about 21 responses, many of which were either by me or by friends who I pressured to submit. Of those, 15 were playlists while 6 were tracks.

In the end, I believe the total amount of songs submitted were just over a thousand, and most songs occurred only once. I decided to create a main playlist for the top 200-or-so songs, [Afmælis!](https://open.spotify.com/playlist/4AOfAjIFHy1vyLZcaeKZ4c?si=0168334dfce74092), while the rest were added to [Restin](https://open.spotify.com/playlist/5myE3gH74ra1UeHYLsaep7?si=18136a6679cb4032).

The party was fun, and after some tweaking, the playlist was great!
