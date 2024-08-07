"""For collecting links from a csv file and updating the "database": songs.csv 
in accordance to what links from Lög.csv have not been accounted for. 
oldforms.txt keeps hold of what links in Lög.csv have already been accounted for.

#need to fix that if songs from a link have been added to the database, another submission of the same link wont be accounted for.
# basically keep a file containing all links already checked."""

import csv
from afmalis import all_songs_from_playlist_id

CSVFILE = "playlists.csv"
SITE = "https://open.spotify.com/"
STORAGE = "songs.csv"


def findformsnr():
    try:
        with open("oldforms.txt") as forms:
            for line in forms:
                return int(line)

    except FileNotFoundError:
        return 0


formsreadto = (
    findformsnr()
)  # to keep track of which links in the Lög.csv file i have already collected from. That way I wont check the same line twice.


def update_forms_nr(counter, formsreadto):
    with open("oldforms.txt", "w") as forms:
        forms.write(
            str(counter + formsreadto)
        )  # updates the oldforms.txt file to the current line of Lög.csv, saying that I checked every line currently in Lög.csv


def opencsvfile(directory, forms):
    with open(directory) as file:
        lines = []
        reader = csv.reader(file)
        for index, line in enumerate(reader):
            if index >= forms and index > 0:
                lines.append(line)
    return lines


def get_all_songs():
    try:
        with open(STORAGE, "r") as file:
            reader = csv.reader(file)
            songdict = {}
            for line in reader:
                if len(line) > 0:
                    songdict[line[0]] = int(line[1])
        return songdict
    except FileNotFoundError:
        return {}


def add_songs(songdict):
    with open(STORAGE, "w") as file:
        writer = csv.writer(file)
        for song in songdict:
            writer.writerow((song, songdict[song]))

    print(f"songs added to {STORAGE}")


def update_songdict(songlist, songdict):
    for song in songlist:
        if song in songdict:
            songdict[song] += 1
        else:
            songdict[song] = 1
    return songdict


if __name__ == "__main__":
    print(f"grabbing the *new* links from {CSVFILE}...")
    lines = opencsvfile(CSVFILE, formsreadto)
    print(f"found {len(lines)} new links")

    print("getting all previously saved songs...")
    songdict = get_all_songs()
    print(f"found {len(songdict)} songs")
    print("adding songs from link to saved songs...")
    for line in lines:
        link = line[1][len(SITE) :]
        slash = link.find("/")
        qm = link.find("?")
        id = link[slash + 1 : qm]
        try:
            if link.startswith("playlist"):
                songuri = all_songs_from_playlist_id(id)

            elif link.startswith("track"):
                songuri = [
                    f"spotify:track:{id}"
                ] * 100  # ensure specially added songs are included
        except Exception as e:
            print(f"error: {e}")
            continue

        songdict = update_songdict(songuri, songdict)

    add_songs(songdict)

    update_forms_nr(len(lines), formsreadto)
