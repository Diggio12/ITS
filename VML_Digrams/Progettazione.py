from enum import *

class Genere(StrEnum):
    uomo = auto()
    donna = auto()

if __name__ == '__main__':
    print(Genere.uomo)
    print(Genere.donna)
    print(Genere.donna.upper())