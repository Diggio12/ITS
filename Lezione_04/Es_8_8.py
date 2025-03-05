
album:dict = {}
def make_album():
    while True:
        opzione:str = input('Inserire "continua" per inserire nuovo album ed artista, premere "esci" per visualizzarli: ')
        if opzione == 'esci':
            break
        elif opzione == 'continua':
            artist_name = input('Inserire nome artista: ')
            album_name = input('Inserire nome album: ')
            album[artist_name] = album_name
        else:
            print('Comando non riconosciuto')
            continue
    return print(album)

make_album()