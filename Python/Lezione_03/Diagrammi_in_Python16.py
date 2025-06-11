i = 0
numeri_pari = 0
numeri_dispari = 0
numeri_positivi = 0
numeri_negativi = 0
j = 0
k = 0
p = 0
d = 0

while i < 10:
    numeri:int = int(input('Inserire un valore: '))
    if numeri % 2 == 0 and numeri > 20:
        p += 1
        numeri_pari = p
    elif numeri % 2 == 1 or numeri < -10:
        d += 1
        numeri_dispari = d
    elif numeri > 0:
        k += 1
        numeri_positivi = k
    elif numeri < 0:
        j += 1
        numeri_negativi = j
    i += 1

print(f'Il numero di numeri positivi è: {numeri_positivi}\nI numeri negativi sono {numeri_negativi}\nI numeri pari maggiori di 20 sono {numeri_pari}\nI numeri dispari sono {numeri_dispari}')

