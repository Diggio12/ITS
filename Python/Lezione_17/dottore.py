from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name, last_name, specialization: str, parcel: float):
        super().__init__(first_name, last_name)

        if isinstance(specialization, str) == False:
            self.__specialization = None
            raise ValueError('La specializzazione inserita non è una stringa!')
            

        elif isinstance(parcel, float) == False:
            self.__parcel = None
            raise ValueError('La parcella inserita non è un float!')
        
        else:
            self.setSpecialization(specialization)
            self.setParcel(parcel)

        
    def setSpecialization(self, specialization: str) -> None:
        if isinstance(specialization, str) == False:
            raise ValueError('La specializzazione inserita non è una stringa!')
        else:
            self.__specialization = specialization


    def setParcel(self, parcel: float) -> None:
        if isinstance(parcel, float) == False:
            raise ValueError('La parcella inserita non è un float!')
        else:
            self.__parcel = parcel

    def getSpecialization(self) -> str:
        return self.__specialization
    
    def getParcel(self) -> float:
        return self.__parcel
    
    def isAValidDoctor(self):
        if self.__age > 30:
            print(f'Doctor {self.__first_name} {self.__last_name} is valid!')
            return True
        else:
            print(f'Doctor {self.__first_name} {self.__last_name} is not valid')

    def doctorGreet(self):
        super().greet()
        print(f'Sono un medico {self.__specialization}')
