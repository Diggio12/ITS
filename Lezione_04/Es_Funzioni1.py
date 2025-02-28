def calcolo_somma(x, y):
    somma:int = 0
    for valori in range (x, y+1):
        somma += valori
    return somma

print(f'La somma dei numeri tra 1 e 10 è: {calcolo_somma(1, 10)}' )

print(f'La somma dei numeri tra 20 e 37 è: {calcolo_somma(20, 37)}')

print (f'La somma dei numeri tra 35 e 49 è: {calcolo_somma(35, 49)}')


