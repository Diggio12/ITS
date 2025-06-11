numero:int = int(input('Inserire numero: '))
somma = 0 

if numero % 1 == 0 and numero > 0:
    for i in range(numero + 1):
        somma = somma + (i*i)
else:
    print('Errore, devi inserire un numero intero positivo')    

print(somma)