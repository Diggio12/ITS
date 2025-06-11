nome:str = input('Inserire nome: ')
gender:str = input('Inserire gender. Digitare m per maschio e f per femmina: ')

match gender:
    case 'm':
        print(f'Nome: {nome}\nGender: Maschio')
    case 'f':
        print(f'Nome: {nome}\nGender: Femmina')
    case _:
        print(f'Mi dispiace {nome}, non è possibile procedere con la generazione di un documento di identità!')