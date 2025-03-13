n:int = int(input('Inserire valore: '))
somma_p:int = 0
somma_d:int = 0

if n >= 1 and n <= 100:
    if n % 2 == 0:    
        for i in range (0, n + 1, 2):
            somma_p += i
    elif n % 2 == 1:
        for x in range (1, n+ 1, 2):
            somma_d = somma_d + x
elif n == 0 or n < 0:
    print('Errore')

print(somma_p, somma_d)