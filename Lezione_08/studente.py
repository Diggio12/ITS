from persona import Persona

class Studente(Persona):

    def __init__(self, name:str, lastname:str, age:int, matricola:str):
        super().__init__(name, lastname, age)

        self.setMatricola(matricola)

    def setMatricola(self, matricola:str) -> None:
        if matricola:
            self.matricola = matricola
        else:
            print('Errore!\nLa matricola non può essere rappresentta da una stringa vuota!')

    def getMatricola(self) ->str:
        return self.matricola
    
    def __str__(self):
        return super().__str__() + f'\nMatricola: {self.matricola}'