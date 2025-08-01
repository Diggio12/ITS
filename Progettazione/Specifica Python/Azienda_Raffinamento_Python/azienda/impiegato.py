from datetime import date
from custom_types import RealGEZ
from progetto import Progetto
from dipartimento import Dipartimento

class Impiegato:
    _nome: str # noto alla nascita
    _cognome: str # noto alla nascita
    _nascita: date # <<immutable>>, noto alla nascita
    _stipendio: RealGEZ # noto alla nascita
    _coinvolto: set[Progetto]
    _direzione: set[Dipartimento]


    def __init__(self, nome: str, cognome: str, nascita: date, stipendio: RealGEZ,) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)

    def nome(self) -> str:
        return self._nome

    def cognome(self) -> str:
        return self._cognome

    def nascita(self) -> date:
        return self._nascita

    def stipendio(self) -> RealGEZ:
        return self._stipendio
    
    def coinvolto(self):
        return set[self._coinvolto]
    
    def direzione(self):
        return set[self._direzione]

    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_cognome(self, c: str) -> None:
        self._cognome: str = c

    def set_stipendio(self, s: RealGEZ) -> None:
        self._stipendio = s

    def set_coinvolto(self, coinvolto: set[Progetto]):
        self._coinvolto = frozenset[coinvolto]

    def set_direzione(self, direzione: set[Dipartimento]):
        self._direzione = frozenset[direzione]