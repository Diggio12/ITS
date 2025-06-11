def compoundInterest(m:int, t:int) -> int:
    m = 1.005 * m
    if t == 0:
        return m
    
    t -= 1

    return compoundInterest(m, t)

print(compoundInterest(1, 6))