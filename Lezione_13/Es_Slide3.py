def sumInRange(a, b):
    sum:int = 0
    if a > b:
        variabile_temporanea = a
        a = b
        b = variabile_temporanea
    while b >= a:
        sum = sum + b
        b = b - 1
    return int(sum)

print(sumInRange(5, 10))
print(sumInRange(10, 5))