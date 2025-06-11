def verifica_combinazione(x: bool, y: bool, z: bool):
    if x == True:
        if y == True or z == True:
            print('Azione Permessa!')
        else:
            print('Azione negata!')
    else:
        print('Azione Negata!')

verifica_combinazione(True, True, False)
verifica_combinazione(False, True, True)
