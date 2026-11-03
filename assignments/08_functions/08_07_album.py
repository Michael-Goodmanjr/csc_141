# Mike Goodman 
# Album 
# 7/10 

def make_album(artist, title, songs=None):
    album = {
        'artist': artist,
        'title': title,
    }

    if songs:
        album['songs'] = songs

    return album

album1 = make_album('Drake', 'Views')
album2 = make_album('Kendrick Lamar', 'DAMN.')
album3 = make_album('Travis Scott', 'Astroworld', 17)

print(album1)
print(album2)
print(album3)
