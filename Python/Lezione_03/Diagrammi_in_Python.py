#1-1
massimo_posti:int = int(input('Posti massimi: '))


posti_disponibili:int = massimo_posti

while True:
    opzione:str = input('Scegliere azione tra ingresso, uscita, stato oppure inserire esci: ')
    if opzione == "ingresso":
        if posti_disponibili > 0:
            posti_disponibili:int = posti_disponibili - 1
        else:
            print('Non ci sono posti disponibili')
    elif opzione == "uscita":
        if posti_disponibili < massimo_posti:
            posti_disponibili:int = posti_disponibili + 1
        else:
            print('Tutti i posti sono liberi')
    elif opzione == "stato":
        posti_occupati: int = massimo_posti-posti_disponibili
        print(f'I posti occupati sono : {posti_occupati}, mentre quelli disponibili sono : {posti_disponibili}')
    elif opzione == "esci":
        break
    else:
        print('Opzione non disponibile')

#1-2
soglia:int = 70
Nord_Sud = 0
Est_Ovest = 0


