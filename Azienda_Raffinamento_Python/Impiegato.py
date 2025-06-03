from datetime import date
from My_types import RealGez
class Impiegato:
    _nome: str
    _cognome: str
    _nascita: date
    _stipendio: RealGez

    def nome(self) -> str:
        return self._nome
    
    def cognome(self) -> str:
        return self._cognome
    
    def nascita(self) -> date:
        return self._nascita
    
    def stipendio(self) -> RealGez:
        return self._stipendio
    
    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_cognome(self, c: str) -> None:
        self._cognome: str = c

    def set_stipendio(self, s: RealGez) -> None:
        self._stipendio = s
