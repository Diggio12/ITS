class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.Restaurant_name = restaurant_name
        self.Cuisine_type = cuisine_type

    def describe_restaurant(self) -> str:
        print(f'The restaurant name is: {self.Restaurant_name} and the cuisine type is: {self.Cuisine_type}')
    
    def open_restaurant(self) -> str:
        print(f'{self.Restaurant_name} is now open!\n')

    

restaurant = Restaurant('Pizza de roma', 'Carbonara')

restaurant.describe_restaurant()
restaurant.open_restaurant()
    