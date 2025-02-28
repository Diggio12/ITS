giorno:int = int(input('Inserire giorno: '))
mese:str = int(input('Inserire mese: '))

giorni:tuple = (giorno, mese)

match giorni:
    case (1, 1):
        print('"Capodanno"')
    case (14, 2):
        print('"San Valentino"')
    case (2, 6):
        print('"Festa della repubblica"')
    case (15, 8):
        print('"Ferragosto"')
    case (31, 10):
        print('"Halloween"')
    case (25, 12):
        print('"Natale"')
    case _:
        print('"Nessuna festività in questa data"')