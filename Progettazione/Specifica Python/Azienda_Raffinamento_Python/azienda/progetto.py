from custom_types import *
from impiegato import Impiegato

class Progetto:
    _nome: str #noto alla nascita
    _budget: RealGEZ #noto alla nascita
    _coinvolto: set[Impiegato]

    def __init__(self, nome: str, budget: RealGEZ):
        self.set_nome(nome)
        self.set_budget(budget)

    def set_nome(self, nome:str):
        self._nome = nome

    def set_budget(self, budget: RealGEZ):
        self._budget = budget

    def set_coinvolto(self, coinvolto: set[Impiegato]):
        self._coinvolto = frozenset[coinvolto]

    def get_nome(self):
        return self._nome
    
    def get_budget(self):
        return self._budget
    
    def get_coinvolto(self):
        return set[self._coinvolto]