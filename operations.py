import foldercalc
import afmalis
import json




def get_songs_from_csv():
    data = foldercalc.get_all_songs()
    songlist = [(i[0], i[1]) for i in data.items() if i[1] >= 1]
    return songlist


def sort_songlist(songlist):
    newsonglist = [i[0] for i in sorted(songlist,key=lambda tup: tup[1], reverse=True)]
    newsonglist = [i for i in newsonglist if not i.__contains__(':local:::')]
    return newsonglist

if __name__ == "__main__":
    songlist = get_songs_from_csv()
    songlist = sort_songlist(songlist)
    playlist_id = afmalis.find_id_from_link('https://open.spotify.com/playlist/1vUJEB69EgPZck5xCUf0kd?si=8a34c7162e5948ae')
    #afmalis.remove_songlist_from_playlist(songlist, playlist_id)
    afmalis.add_songlist_to_playlist(songlist, playlist_id)






    # for song in songlist:
    #     print(song)
    
    
