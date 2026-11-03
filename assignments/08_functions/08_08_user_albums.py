# Mike Goodman 
# user albums 
# 8/10 

def make_album(artist, title):
    album = {
        'artist': artist,
        'title': title,
    }

    return album

while True:
    print("\nEnter an album's information.")
    print("Enter 'q' at any time to quit.")

    artist = input("Artist name: ")

    if artist == 'q':
        break

    title = input("Album title: ")

    if title == 'q':
        break

    album = make_album(artist, title)

    print(album) 