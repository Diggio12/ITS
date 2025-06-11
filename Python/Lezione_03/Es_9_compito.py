pi:float = 0
i:int = 1
j:int = 0
counter = 0

while True:                            #ciclo while per ciclare
    if str(pi)[:4] == "3.14":
        print(f'Valore di 3.14 raggiunto. I termini necessari per raggiungerlo sono stati {j}')
        break
    else:
        pi = pi + (4/i)                  #prima ripetizione dove aggiorno pi facendo addizione con 4/i, aggiorno j ed i
        j += 1
        i += 2
        if str(pi)[:4] == "3.14":
            print(f'Valore di 3.14 raggiunto. I termini necessari per raggiungerlo sono stati {j}')
            break
        print(pi, j)
        pi = pi - (4/i)                  #seconda ripetizione dove aggiorno pi facendo sottrazione con 4/i, aggiorno j ed i
        j += 1
        i += 2
        counter +=1
        print(pi, j)
pi:float = 0
i:int = 1
j:int = 0
counter = 0
while True:                           
    if str(pi)[:5] == "3.141":
        print(f'Valore di 3.141 raggiunto. I termini necessari per raggiungerlo sono stati {j}')
        break
    else:
        pi = pi + (4/i)                  
        j += 1
        i += 2
        if str(pi)[:5] == "3.141":
            print(f'Valore di 3.141 raggiunto. I termini necessari per raggiungerlo sono stati {j}')
            break
        pi = pi - (4/i)                  
        j += 1
        i += 2
while True:                            
    if str(pi)[:6] == "3.1415":
        print(f'Valore di 3.1415 raggiunto. I termini necessari per raggiungerlo sono stati {j}')
        break
    else:
        pi = pi + (4/i)                  
        j += 1
        i += 2
        pi = pi - (4/i)                  
        j += 1
        i += 2

pi:float = 0
i:int = 1
j:int = 0
counter = 0
while True:                            
    if str(pi)[:7] == "3.14159":
        print(f'Valore di 3.14159 raggiunto. I termini necessari per raggiungerlo sono stati {j}')
        break
    else:
        pi = pi + (4/i)                  
        j += 1
        i += 2
        if str(pi)[:7] == "3.14159":
            print(f'Valore di 3.14159 raggiunto. I termini necessari per raggiungerlo sono stati {j}')
            break
        pi = pi - (4/i)                  
        j += 1
        i += 2