i:int = 0
somma:float = 0
media_voti:float = 0

while True:
    scelta:str = input('Digitare "si" per inserire un nuovo voto.\nDigitare "no" per vedere la media dei voti: ')
    match scelta:
        case 'si':
            voto:float = float(input('Inserire voto: '))
            if voto > 0:
                i += 1
                somma = somma + voto
                print('Voto inserito con successo!')
            else:
                print('Errore, non è possibile inserire questo voto')
        
        case 'no':
            if i > 0:
                media_voti = somma / i
                print(f'La media dei voti equivale a: {media_voti:.1f}')
                break
            else:
                print('Nessun voto inserito')

