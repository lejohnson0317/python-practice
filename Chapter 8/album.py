def make_album(artist_name, album_name, number_songs=None):
    """Building a dictionary of a music album"""
    album = {'artist': artist_name, 'album': album_name}
    if number_songs:
        album['number_songs'] = number_songs
    return album

music = make_album('Jimi Hendrix', 'Are you experienced')
print(music)
music = make_album('Prince', 'Purple Rain', 10)
print(music)
music = make_album('Pink Floyd', 'The Wall', 15)
print(music)
