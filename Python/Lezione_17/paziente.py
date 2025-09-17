from persona import Persona

class Paziente(Persona):
    def __init__(self, first_name, last_name, Id_code: str):
        super().__init__(first_name, last_name)

        self.setIdCode(Id_code)

    def setIdCode(self, Id_code: str) -> None:
        self.__Id_code = Id_code

    def getIdCode(self) -> str:
        return self.__Id_code
    
    def patientInfo(self) -> str:
        print(f'Paziente: {self.__first_name} {self.__last_name}\nID: {self.__Id_code}')