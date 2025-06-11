età:int = int(input('Inserire la propria età: '))

match età:
    case età if età >= 18 and età <= 65:
        print("Può partecipare all'attività")
    case età if età < 18:
        print('Età minima non raggiunta')
    case età if età > 65:
        print('Età massima superata')





