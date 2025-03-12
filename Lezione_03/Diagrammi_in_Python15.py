n:int = int(input('Inserire valore: '))
somma_p:int = 0
somma_d:int = 0

if n >= 1 and n <= 100:
    for i in range (1, n):
        if n % 2 == 0:
            somma_p = somma_p + i
        else:
            somma_d = somma_d + i
elif n == 0 or n < 0:
    print('Errore')