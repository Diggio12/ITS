import math 


def calculateCharges(macchina: int):
    tariffa: float = 2.00
    ore: int = int(input('Inserire tempo in ore passato nel parcheggio: '))
    parcheggio: list = [macchina, ore, tariffa]
    i = 0

    if ore <= 3:
        parcheggio[2] = tariffa
    elif ore == 24:
        tariffa = 10.00
        parcheggio[2] = tariffa
    else:
        while i <= ore:
            if tariffa == 10:
                break
            else:
                tariffa += 0.50
                parcheggio[2] = tariffa
                i += 1

    return parcheggio

mat: list[list] = []
c1 = calculateCharges(1)
c2 = calculateCharges(2)
c3 = calculateCharges(3)
c4 = calculateCharges(4)

mat.append(['Car', 'Hours', 'Charge'])
mat.append(c1)
mat.append(c2)
mat.append(c3)
mat.append(c4)
mat.append(['TOTAL', c1[1] + c2[1] + c3[1] + c4[1], c1[2] + c2[2] + c3[2] + c4[2]])


for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(f"{mat[i][j]:<10}", end='')
    print('\n')
