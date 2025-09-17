class Persona:
    def __init__(self, first_name: str, last_name: str):
        
        if not isinstance(first_name, str) and not isinstance(last_name, str):
            self.setName(first_name)
            self.setLastName(last_name)
            self.setAge = None

        elif isinstance(first_name, str) and isinstance(last_name, str):
            self.setName(first_name)
            self.setLastName(last_name)
            self.__age = 0
        
        elif isinstance(first_name, str) == False:
            raise ValueError('Il nome inserito non è una stringa!')
            self.__first_name = None
        
        elif isinstance(last_name, str) == False:
            raise ValueError('Il cognome inserito non è una stringa!')
            self.__last_name = None


    def setName(self, first_name: str) -> None:
        if isinstance(first_name, str) == False:
            raise ValueError('Il nome inserito non è una stringa!')
        else:
            self.__first_name = first_name


    def setLastName(self, last_name: str) -> None:
        if isinstance(last_name, str) == False:
            raise ValueError('Il cognome inserito non è una stringa!')
        else:
            self.__last_name = last_name

    def setAge(self, age: int) -> None:
        if isinstance(age, int) == False:
            raise ValueError("L'età inserita non è un intero!")
        else:
            self.__age = age


    def getName(self) -> str:
        return self.__first_name
    
    def getLastName(self) -> str:
        return self.__last_name
    
    def getAge(self) -> int:
        return self.__age
    
    def greet(self):
        print(f'Ciao, sono {self.__first_name} {self.__last_name}! Ho {self.__age} anni!')

