oggetti:list = []

while len(oggetti) < 3:
    oggetti.append(input('Inserire oggetto: '))

match oggetti:
    case ['penna', 'matita', 'quaderno']:
        print('Materiale scolastico')
    case ['pane', 'latte', 'uova']:
        print('Prodotti alimentari')
    case ['sedia', 'tavolo', 'armadio']:
        print('Mobili')
    case ['telefono', 'computer', 'tablet']:
        print('Dispositivi elettronici')
    case _:
        print('Categoria sconosciuta')