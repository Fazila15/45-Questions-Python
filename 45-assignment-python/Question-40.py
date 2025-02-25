# Function to create an album dictionary
def make_album(artist, title, tracks=None):
    album = {
        'artist': artist,
        'title': title,
    }
    if tracks:
        album['tracks'] = tracks
    return album

# Creating three album dictionaries
album1 = make_album('Taylor Swift', '1989')
album2 = make_album('Adele', '25', 11)
album3 = make_album('Ed Sheeran', 'Divide', 12)

# Printing the album dictionaries
print(album1)
print(album2)
print(album3)
