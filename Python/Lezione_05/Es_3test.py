def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    somma_liste: list[int] = []
    i: int = 0
    while i < len(x):
        z = x[i] + y[i]
        somma_liste.append(z) 
        i+=1   
    return somma_liste