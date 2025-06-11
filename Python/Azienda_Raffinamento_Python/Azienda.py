from enum import *
from My_types import *

class Genere(StrEnum):
    uomo = auto()
    donna = auto()


class Indirizzo:
    
    def __init__(self, via:str, civico:str, cap: str):
        if not isinstance(via, str) or not isinstance(civico, str) or not isinstance(cap, str):
            raise TypeError("Non hai inserito dati validi per un indirizzo")
        
        self.via = via
        self.civico = civico
        self.cap = cap

    def get_via(self):
        return self.via
    
    def get_civico(self):
        return self.civico
    
    def get_cap(self):
        return self.cap
    
    def __hash__(self):
        return hash((self.get_via(), self.get_civico(), self.get_cap()))
    
    def __eq__(self, other)->bool:
        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):
            return False
        return (self.get_via(), self.get_civico(), self.get_cap()) == (other.get_via(), other.get_civico(), other.get_cap())
        


class Telefono:

    def __init__(self, numero):
        if len(numero) != 10 and numero.isdigit():
            raise TypeError("Numero telefono non valido")
        
        self.numero = numero
    
    def get_numero(self):
        return self.numero
    
    def __hash__(self):
        return hash(self.get_numero())
    
    def __eq__(self, other):
        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):
            return False
        return (self.get_numero()) == (other.get_numero())