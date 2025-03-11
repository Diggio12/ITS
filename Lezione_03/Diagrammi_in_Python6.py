x:int = int(input('Inserire valore x: '))
somma_pari:int = 0
somma_dispari:int = 0

if x > 0:
    for i in range (10):
        numeri = int(input('Inserire numero: '))
        if x % 2 == 0:
            if numeri > (x/2):
                somma_pari = somma_pari + numeri
        else:
            if numeri < x:
                somma_dispari = somma_dispari + numeri
else:
    print('Errore x deve essere positivo')

print(somma_dispari, somma_pari)