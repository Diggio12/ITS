voto:int = int(input('Inserire il voto: '))

match voto:
    case voto if voto >= 1 and voto <=3:
        print('Output: "Gravemente insufficiente"')
    case voto if voto == 4 or voto == 5:
        print('Output: "Insufficiente"')
    case voto if voto == 6 or voto == 7:
        print('Output: "Sufficiente"')
    case voto if voto == 8 or voto == 9:
        print('Output: "Molto buono"')
    case voto if voto == 10:
        print('Output: "Eccellente"')
    case _:
        print('"Voto non valido"')
        