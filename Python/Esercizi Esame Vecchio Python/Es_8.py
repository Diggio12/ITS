class Movie:

    def __init__(self, movie_id: str, title: str, director: str, is_rented = False):
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented

    def rent(self) -> None:
        if self.is_rented == True:
            print(f'Il film {self.title} è già noleggiato')
        else:
            self.is_rented = True

    def return_movie(self) -> None:
        if self.is_rented == True:
            self.is_rented = False
        else:
            print(f'Il film {self.title} non è stato noleggiato da questo cliente')

    
class Customer:

        def __init__(self, customer_id: str, name: str):
            self.customer_id = customer_id
            self.name = name
            self.rented_movies: list[Movie] = []

        def rent_movie(self, movie: Movie) -> None:
            if movie.is_rented == False:
                self.rented_movies.append(movie)
            else:
                print(f'Il film {movie.title} è già stato noleggiato')

        def return_movie(self, movie: Movie) -> None:
            if movie in self.rented_movies:
                self.rented_movies.remove(movie)
                movie.return_movie()
            else:
                print(f'Il film {movie.title} non è stato noleggiato da questo cliente')

    
class VideoRentalStore:

    def __init__(self, movies: dict[str, Movie] = {}, customers: dict[str, Customer] = {}):

            self.movies = movies
            self.customers = customers

    def add_movie(self, movie_id: str, title: str, director: str) -> None:

        if movie_id not in self.movies:

            self.movies[movie_id] = Movie[movie_id, title, director]

        else:
            print(f'Il film con ID {movie_id} esiste già')

    def register_customer(self, customer_id: str, name: str) -> None:
        if customer_id not in self.customers:
            self.customers[customer_id] = Customer[customer_id, name]

        else:
            print(f'Il cliente con ID {customer_id} è già registrato')

    def rent_movie(self, customer_id: str, movie_id: str) -> None:
        
        if movie_id in self.movies and customer_id in self.customers:
            self.customers[customer_id].rent_movie(self.movies[movie_id])
        else:
            print(f'Cliente o Film non trovato')

    def return_movie(self, customer_id: str, movie_id: str) -> None:
        
        if movie_id in self.movies and customer_id in self.customers:
            self.customers[customer_id].return_movie(self, self.movies[movie_id])
        else:
            print('Cliente o film non trovato')

    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        if customer_id in self.customers:
            return self.customers[customer_id].rented_movies
        else:
            print('Cliente non trovato')
            return []
        
    def get_all_movies(self) ->list[Movie]:
        
        film_noleggiati: list[Movie] = []

        for customer_id, customer in self.customers.items():

            film_noleggiati += customer.rented_movies
        
        return film_noleggiati
