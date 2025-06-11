#ciclo while
max:int = int(input('Inserire valore: '))
cont:int = 1

while cont < 4:
    cont += 1
    n:int = int(input('Inserire numero: '))
    if n > max:
        max = n

print(max)

#ciclo repeat
max:int = int(input('Inserire primo valore: '))
cont:int = 1

n:int = int(input('Inserisci numero: '))
if n > max:
    max = n
while True:
    
    cont += 1
    n:int = int(input('Inserire valore: '))
    if n > max:
        max = n
    if cont == 4:
        break

print(max)

#ciclo for

max:int = int(input('Inserire massimo: '))

for valore in range (0, 5):
    n:int = int(input('Inserire valore: '))

    if n > max:
        max = n

print(max)

