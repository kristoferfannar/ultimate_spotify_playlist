import foldercalc
import afmalis


def get_songs_from_csv():
    data = foldercalc.get_all_songs()
    songlist = [(i[0], i[1]) for i in data.items()]
    return songlist


def sort_songlist(songlist):
    newsonglist = [i[0] for i in sorted(songlist, key=lambda tup: tup[1], reverse=True)]
    newsonglist = [i for i in newsonglist if not i.__contains__(":local:")]
    print(len(newsonglist))
    return newsonglist


if __name__ == "__main__":
    songlist = get_songs_from_csv()
    songlist = sort_songlist(songlist)[:200]
    playlist_id = afmalis.find_id_from_link(
        input("paste a link of a playlist of yours you'd like to overwrite: ")
    )

    print("playlist id: ", playlist_id)
    afmalis.clear_playlist(playlist_id)

    print(f"adding {len(songlist)} songs...")
    afmalis.add_songlist_to_playlist(songlist, playlist_id)
