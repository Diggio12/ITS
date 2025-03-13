valore_iniziale:int = int(input('Inserire valore iniziale: '))
somma_p:int = 0
prodotto_d:int = 1

if valore_iniziale % 2 == 0:
    for x in range (1, valore_iniziale + 1):
        if x % 4 == 0:
            somma_p += x
elif valore_iniziale % 2 == 1:
    for i in range (1, valore_iniziale +1, 2):
        prodotto_d = prodotto_d * i
elif valore_iniziale < 0:
    print('Errore!')

print(f'La somma dei numeri pari divisibili per 4 è: {somma_p}\nIl prodotto dei numeri dispari è: {prodotto_d}')

