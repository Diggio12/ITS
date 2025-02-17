
album_dict_1:dict = {}
album_dict_2:dict = {}
album_dict_3:dict = {}

def make_album(artist_name, album_title):
    album_dict = {}
    album_dict[artist_name] = album_title
    return album_dict

artist_name:str = input('Insert artist name: ')
album_title:str = input('Insert album title: ')

album_dict_1 = make_album(artist_name, album_title)

print(album_dict_1)

artist_name_2:str = input('Insert artist name: ')
album_title_2:str = input('Insert album title: ')

album_dict_2 = make_album(artist_name_2, album_title_2)

print(album_dict_2)

artist_name_3:str = input('Insert artist name: ')
album_title_3:str = input('Insert album title: ')

album_dict_3 = make_album(artist_name_3, album_title_3)

print(album_dict_3)