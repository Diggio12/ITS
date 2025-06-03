from Azienda_Raffinamento_Python.Azienda import *
from My_types import *

class Dipartimento:
    _nome :str
    _telefoni: set[Telefono]
    _indirizzo: Indirizzo | None

    def nome(self) -> str:
        return self.nome
    
    def indirizzo(self) -> Indirizzo | None:
        return self._indirizzo

    def telefoni(self) -> set[Telefono]:
        return self._telefoni
    
    def set_indirizzo(self, i: Indirizzo | None) -> None:
        self._indirizzo = i

    def add_telefono(self, telefono: Telefono) -> None:
        self._telefoni.add(telefono)

    def remove_telefono(self, telefono: Telefono) -> None:
        if len(self._telefoni) >= 2:
            self._telefoni.remove(telefono)
        else:
            raise RuntimeError('Il dipartimento deve avere almeo un numero di telefono!')
        
    