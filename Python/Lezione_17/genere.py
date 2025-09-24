from film import Film

class Azione(Film):
    def __init__(self, Id_Code, title):
        super().__init__(Id_Code, title)
        self.__genere = 'Azione'
        self.__penale = 3

    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, numero_giorni_ritardo: int) -> float:
        return numero_giorni_ritardo*self.getPenale()
    

class Commedia(Film):
    def __init__(self, Id_Code, title):
        super().__init__(Id_Code, title)
        self.__genere = 'Commedia'
        self.__penale = 2.50

    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, numero_giorni_ritardo: int) -> float:
        return numero_giorni_ritardo*self.getPenale()
    


class Drama(Film):
    def __init__(self, Id_Code, title):
        super().__init__(Id_Code, title)
        self.__genere = 'Drama'
        self.__penale = 2

    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, numero_giorni_ritardo: int) -> float:
        return numero_giorni_ritardo*self.getPenale()