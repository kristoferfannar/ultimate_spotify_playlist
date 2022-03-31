# ultimate_spotify_playlist
trying to create the absolute best spotify playlist, using Spotify's API.



Plan:
    Creating a playlist for a birthday party, with all the best songs according to birthday guests.
    Birthday guests send their spotify playlist as a link through google forms. 
    I download a csv file from google forms (Playlistar/Lög.csv) with all the playlist information.
    I collect all the songs in all the playlists, including which songs are most popular (in most playlists). (foldercalc.py)
    From that info, I create a playlist of my own with Spotify's API, to create a playlist with all the songs in the birthday guests' playlist. (afmalis.py)
    Everyone wins.




# PS
I get my authentication tokens from a python file I had called secretsAPI, which I won't share since it contains sensitive information (passwords, id's, access codes and so on). They are crucial for getting access to the API so the program wont do much without them.

foldercalc.py can be run without authentication though!