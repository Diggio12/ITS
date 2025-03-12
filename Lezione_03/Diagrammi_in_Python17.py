import math
temperature:dict = {'1': float(input('Inserire temperatura lunedi: ')), '2': float(input('Inserire temperatura martedi: ')), '3': float(input('Inserire temperatura mercoledi: ')), '4': float(input('Inserire temperatura giovedi: ')), '5': float(input('Inserire temperatura venerdi: ')), '6': float(input('Inserire temperatura sabato: ')), '7': float(input('Inserire temperatura domenica: '))}
temp_min:float = math.inf
temp_max:float = -math.inf
giorno_max:str = ''
giorno_min:str = ''
media_temp:float = 0
somma_temp:float = 0
norma:int = 0

for key, value in temperature.items():
    somma_temp = somma_temp + value
    if value >= 10 and value <= 30:
        norma += 1
    elif value > 35 or value < 5:
        print('Allerta temperatura!')
    
    if value > temp_max:
        temp_max = value
        giorno_max = key
    elif value < temp_min:
        temp_min = value
        giorno_min = key

media_temp = somma_temp / 7

print(f'La temperatura medio è di {media_temp:.1f}°\nIl giorno con la temperatura massima è {giorno_max}\nIl giorno con la temperatura minima è {giorno_min}')