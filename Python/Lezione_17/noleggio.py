from film import Film
from genere import *

class Noleggio:
    def __init__(self, film_list: list[Azione | Commedia | Drama]):
        self.__film_list = film_list
        self.rented_film: dict = {}

    def isAvaible(self, film: Azione | Commedia | Drama) -> bool:
        if film in self.__film_list:
            print(f'Il film scelto è disponibile: {film.getTitle()}')
            return True
        else:
            print(f'Il film scelto non è disponibile: {film.getTitle()}')


    def rentAMovie(self, film: Azione | Commedia | Drama, clientId):
        if film in self.__film_list:
            self.__film_list.remove(film)
            print(f'Il cliente {clientId} ha noleggiato {film}!')
            if clientId in self.rented_film:    
                self.rented_film[clientId].append(film)
            else:
                self.rented_film[clientId] = [film]
        else:
            print(f'Non è possibile noleggire il film {film}')


    def giveBack(self, film: Azione | Commedia | Drama, clientId, days):

        self.rented_film[clientId].remove(film)

        self.__film_list.append(film)
        
        totale_penale = film.calcolaPenaleRitardo(days)

        print(f'Cliente: {clientId}! La penale da pagare per il film {film} è di {totale_penale} euro!')


    def printMovies(self):
        for i in self.__film_list:
            print(f'{i.getTitle} - {i.getGenere} -')

    def printRentMovies(self, clientId):
        if clientId in self.rented_film:
            for film in self.rented_film[clientId]:
                print(film)

        else:
            print('Non si hanno film rent a proprio carico')