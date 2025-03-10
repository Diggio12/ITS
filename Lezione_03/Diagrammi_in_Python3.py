massimo_posti:int = 100
posti_liberi:int = 100
posti_occupati:int = 0
nome_corso:str = input('Inserire nome corso: ')

while True:
    opzione:str = input('per iscriversi al corso digitare "iscrivi"\nper annullare iscrizione al corso digitare "annulla"\nper visualizzare posti disponibili digitare "visualizza".\nDigitare "elimina" per selezionare un nuovo corso.\nDigitare "esci" per terminare il programma: ')

    match opzione:
        case 'iscrivi':
            if posti_liberi > 0:
                posti_liberi -= 1
                posti_occupati += 1
            else:
                print('Non ci sono posti liberi')
        case 'annulla':
            if posti_occupati > 0:
                posti_liberi += 1
                posti_occupati -= 1
            else:
                print('Il corso non ha posti occupati')
        case 'visualizza':
            print(f'Il numero di posti liberi è: {posti_liberi}, il numero di posti occupati è: {posti_occupati}')
        case 'elimina':
            nome_corso:str = input('Inserire nome corso: ')
            massimo_posti = 100
        case 'esci':
            break
        case _:
            print('Comando non riconosciuto')
