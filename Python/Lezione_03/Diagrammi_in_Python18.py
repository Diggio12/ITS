valore_numero:int = int(input('Inserire valore iniziale: '))
somma:int = 0
media:int = 0
somma_p:int = 0
somma_d:int = 0


for i in range (1, valore_numero + 1):
    numeri:int = int(input('Inserire valore: '))
    somma += numeri
    media = somma/i
    if numeri % 2 == 0 and numeri > media:
        somma_p += numeri
    elif numeri % 2 == 1 or numeri < media:
        somma_d += numeri

if somma_p > somma_d:
    print(f'La somma dei numeri pari è maggiore di quella dispari con una somma totale di: {somma_p}')
else:
    print(f'La somma dei numeri dispari è maggiori di quella pari con una somma totale di: {somma_d}')

print(f'la somma dei numeri pari è: {somma_p}\nla somma dei numeri dispari è: {somma_d}')