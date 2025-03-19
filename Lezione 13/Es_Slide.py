def countdown(n:int) -> None:
    if n < 0:            
        print('Errore. Numero inserito negativo!')
    else:
        while n >= 0:
            print(n)
            n = n -1
            

countdown(5)
countdown(-5)