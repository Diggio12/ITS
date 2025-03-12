x:int = int(input('Inserire valore x: '))
y:int = int(input('Inserire valore y: '))
z:int = int(input('Inserire valore z: '))

if x % 1 == 0 and x > 0:
    if y % 1 == 0 and y > 0:
        if z % 1 == 0 and z > 0:
            if (x+y+z) % 2 == 0 and x % 3 == 0 and y % 5 == 0 and z % 7 == 0:
                print('Regole rispettate')
            else:
                print('Regole non rispettate')
        else:
            print('Il valore z deve essere intero e positivo')
    else:
        print('Il valore di y deve essere intero e positivo')
else:
    print('Il valore di x deve essere intero e positivo')
