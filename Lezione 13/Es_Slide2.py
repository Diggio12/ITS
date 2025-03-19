def sum(n) -> None:
    sum:int = 0
    if n < 0:
        print('Errore! Numero negativo')
        return None
    else:
        while n >= 0:
            sum = sum + n
            n = n - 1
    print(sum)

sum(5)
sum(-5)
