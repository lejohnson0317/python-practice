def make_album(artist_name, album_name):
    """Building a dictionary of a music album"""
    album = {
        'artist': artist_name.title(),
        'album': album_name.title(),
        }
    return album

while True:
    print("\nPlease enter the artist name: ")
    print("enter 'q' to quit")

    artist_name = input("Artist: ")
    if artist_name == 'q':
        break
    album_name = input("Album: ")
    if album_name == 'q':
        break

    music = make_album(artist_name, album_name)
    print(music)
