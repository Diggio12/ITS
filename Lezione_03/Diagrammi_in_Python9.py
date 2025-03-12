numero:int = int(input('Inserire valore: '))
i:int = 0

if numero > 0 and numero % 1 == 0:
    for x in range (10):
        numeri:int = int(input('Inserire nuovi valori: '))
        if numeri % numero == 0:
            i += 1
else:
    print('Errore')

print(f'I numeri divisibili per {numero} sono {i}')