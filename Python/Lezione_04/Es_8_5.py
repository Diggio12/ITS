def describe_city(name, country):
    print(f'{name} is in {country}')

country:str = 'Italy'
name_1:str = input('Insert city name: ')

describe_city(name_1, country)

name_2:str = input('Insert city name: ')

describe_city(name_2, country)

name_3:str = input('Insert city name: ')

describe_city(name_3, country)