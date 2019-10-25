def make_album(artist, album, song_number=None):
    """Display a dictionary with aritist and album."""
    artist_album = {'Artist': artist.title(), 'Album': album.title()}
    if song_number:
        artist_album["Number of Songs"] = song_number
    return artist_album

while True:
    print("Enter 'q' anytime to quit.")
    
    artist_name = input("Enter the artist's name: ")
    if artist_name.lower() == 'q':
        break
    
    album_name = input("Enter the album's name: ")
    if album_name.lower() == 'q':
        break

    song_no = input("Number of songs on the album (optional): ") 
    if song_no.lower() == 'q':
        break
    
    full_result = make_album(artist_name, album_name, song_no)
    print(full_result)

    continue_ = input("Type yes to continue or q to quit: ")
    if continue_ == 'q':
        break
    elif continue_ == 'yes':
        continue
    else:
        print("invalid input: quitting")
        break
