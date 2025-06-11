n:int = int(input('Inserire valore: '))

if n < 2:
    print('Il numero inserito non è primo')
else:
    div:int = 2
    is_prime:bool = True


    while div < n:
        if n % div == 0:
            is_prime = False
            break
        
        div += 1

    if is_prime:
        print('Il numero è primo')
    else:
        print('Il mumero non è primo')