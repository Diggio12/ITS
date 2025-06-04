import random

def random_number():
    range_massimo = int(input('Inserire range massimo: '))
    number: int = random.randint(1, range_massimo)
    tentativi: int = 0

    while True:
        guess_number: int = int(input('Inserire guess del numero: '))
        if guess_number == number:
            tentativi += 1
            print(f'Bravo! Hai indovinato il numero in: {tentativi} tentativi')
            break
        elif guess_number < number:
            tentativi += 1
            print(f'Troppo basso! Sei al: {tentativi} tentativo')
        elif guess_number > number:
            tentativi += 1
            print(f'Troppo alto! Sei al: {tentativi} tentativo')
        elif tentativi > 7:
            print('Tentativi Esauriti!')
            break
        

random_number()
