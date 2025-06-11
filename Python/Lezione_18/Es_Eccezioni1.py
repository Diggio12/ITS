import math

def safe_sqrt(number:int):

    if number < 0:
        raise ValueError(f'The number cannot be negative: {number}')
    else:
        x = math.sqrt(number)
        print(x)
    
safe_sqrt(-9)
