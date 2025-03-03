a:float = float(input('Inserire valore ipotenusa: '))
b:float = float(input('Inserire valore secondo cateto: '))

if a > b:
    c:float = (a**2 - b**2)**(1/2)
    print (f"Il cateto equivale a: {c}")
else:
    print('Errore')

