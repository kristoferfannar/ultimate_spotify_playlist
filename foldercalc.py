"""For collecting links from Lög.csv and updating the database: songs.csv 
in accordance to what links from Lög.csv have not been accounted for. 
oldforms.txt keeps hold of what links in Lög.csv have already been accounted for.

#need to fix that if songs from a link have been added to the database, another submission of the same link wont be accounted for.
# basically keep a file containing all links already checked."""

import csv
from afmalis import all_songs_from_playlist_id

CSVFILE = __file__[:-13] + "Playlistar/Lög.csv"
SITE = 'https://open.spotify.com/'
STORAGE = 'songs.csv'

def findformsnr():
    with open('oldforms.txt') as forms:
        for line in forms:
            return int(line)
formsreadto = findformsnr()

def update_forms_nr(counter, formsreadto):
    with open('oldforms.txt', 'w') as forms:
        forms.write(str(counter+formsreadto))


def opencsvfile(directory, forms):
    with open(directory) as file:
        lines = []
        reader = csv.reader(file)
        for index, line in enumerate(reader):
            if index >= forms and index > 0:
                lines.append(line)
    return lines



def get_all_songs():
    with open(STORAGE, 'r') as file:
        reader = csv.reader(file)
        songdict = {}
        for line in reader:
            if len(line) > 0:
                songdict[line[0]] = int(line[1])
    return songdict


def add_songs(songdict):
    with open(STORAGE, 'w') as file:
        writer = csv.writer(file)
        for song in songdict:
            writer.writerow((song, songdict[song]))        
        

def update_songdict(songlist, songdict):
    for song in songlist:
        if song in songdict:
            songdict[song] += 1
        else:
            songdict[song] = 1
    return songdict






if __name__ == "__main__":
    lines = opencsvfile(CSVFILE, formsreadto)
    #print(lines)
    songdict = get_all_songs()
    for line in lines:
        link = line[1][len(SITE):]
        slash = link.find('/')
        qm = link.find('?')
        id = link[slash+1:qm]
        try:
            if link.startswith('playlist'):
                songuri = all_songs_from_playlist_id(id)

            elif link.startswith('track'):
                songuri = [f'spotify:track:{id}'] * 2
        except KeyError:
            continue



        songdict = update_songdict(songuri, songdict)

    add_songs(songdict)

    update_forms_nr(len(lines), formsreadto)

