from persona import Persona
from studente import Studente

p: Persona = Persona('Mattia', 'Di Giorgio', 22)

print(p)

Studente1: Studente = Studente('Luca', 'Bianconi', 21, '838271')

print(f'\n{Studente1}')

if isinstance(Studente1, Studente):
    print('\nStudente1 è istanza della classe Studente')