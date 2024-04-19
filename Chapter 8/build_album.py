def make_album(artist_name, album_name, number_songs=None):
    """Building a dictionary of a music album"""
    album = {'artist': artist_name, 'album': album_name}
    if number_songs:
        album['number_songs'] = number_songs
    return album