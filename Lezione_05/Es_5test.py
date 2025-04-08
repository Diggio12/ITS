def prime_factors(n: int) -> list[int]:
    numeri_primi:list[int] = []
    i: int = 2
    while n > 1:
        while n % i == 0:
            numeri_primi.append(i)
            n//=i
        i = i + 1
    return numeri_primi