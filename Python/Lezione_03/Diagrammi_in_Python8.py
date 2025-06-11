a:int = int(input('Inserire valore a: '))
b:int = int(input('Inserire valore b: '))
somma:int = 0

if a > 0 and b > 0 and a < b:
    for i in range(a, b + 1):
        somma = somma + i
    print(somma)
else:
    print('Errore, parametri non rispettati')

