
def make_car(nome:str, modello:str, colore:str = None, tow_package:bool = None):
    if colore == None and tow_package == None:
        car:dict = {'produttore': nome, 'modello':modello}
    elif colore == None and tow_package != None:
        car:dict = {'produttore':nome, 'modello':modello, 'tow package':tow_package}
    elif colore != None and tow_package == None:
        car:dict = {'produttore':nome, 'modello':modello, 'colore':colore}
    else:
        car:dict = {'produttore':nome, 'modello':modello, 'colore': colore, 'tow package':tow_package} 
    return car

print (make_car('Miata', 'Mazda', tow_package = True))