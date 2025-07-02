class Media:
    def __init__(self, title: str, reviews: list[int]):
        self.set_title(title)
        self.reviews = reviews

    def set_title(self, title: str):
        self.title = title

    def get_title(self):
        return self.title
    
    def aggiungiValutazione(self, voto: int):
        if voto in range (1, 6):
            self.reviews.append(voto)

    def getMedia(self):
        somma = 0
        for voto in self.reviews:
          somma += voto  
            
        media = somma/len(self.reviews)
        return media
        

    def getRate(self):

        if self.getMedia() <= 1.4:
            return 'Terribile'
        elif self.getMedia() <= 2.4:
            return 'Brutto'
        elif self.getMedia() <= 3.4:
            return 'Normale'
        elif self.getMedia() <= 4.4:
            return 'Bello'
        else:
            return 'Grandioso'
        
    def ratePercentage(self, voto:int):
        i=0
        for x in self.reviews:
            if voto == x:
                i += 1

        return f'La presenza del voto è di: {(i*100)/len(self.reviews)}'
    
    def recensione(self):
        return f'Titolo del Film: {self.title}\nVoto Medio: {self.getMedia()}\nGiudizio: {self.getRate()}\nTerribile: {self.ratePercentage(1)}%\Brutto: {self.ratePercentage(1)}%\nTerribile: {self.ratePercentage(2)}%\Normale: {self.ratePercentage(3)}%\Bello: {self.ratePercentage(4)}%\Grandioso: {self.ratePercentage(5)}%'
    

class Film(Media):
    def __init__(self, title):
        super().__init__(title)