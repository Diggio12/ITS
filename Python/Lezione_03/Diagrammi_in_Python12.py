n:int = int(input('Inserire valore n: '))
somma:int = 0
prodotto:int = 1

for i in range(n):
    x:int = int(input('Inserire valore x: '))
    y:int = int(input('Inserire valore y: '))
    if x > 0 and y > 0:
        prodotto = prodotto + (x*y)
    elif x < 0 and y < 0:
        print('Errore')
    else:
        somma = somma + (x+y)

print(prodotto, somma)