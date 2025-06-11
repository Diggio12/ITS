numero:int = int(input('Inserire valore: '))

if numero % 2 == 0 and numero > 10:
    print('Valore valido')
elif numero % 2 == 1 or numero <= 10:
    print('Valore non valido')