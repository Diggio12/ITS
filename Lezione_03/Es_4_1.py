nice_pizzas:list = ['Margherita', 'Diavola', 'Patate e Salsiccia', 'Quattro Formaggi', 'Capricciosa', 'Ortolana', 'Bianca']
for pizzas in nice_pizzas:
    #print(pizzas)              #basic print of the name of each pizza
    print(f'I like {pizzas} pizza')  #print with a simple statement
i = 0

while i < len(nice_pizzas):
    print(f'I like {nice_pizzas[i]} pizza')
    i += 1

print(f'If I would have to choose between pizzas type, I would say that {nice_pizzas[2]} is my favourite.\n Also {nice_pizzas[0]} is a classic.\n Man I love pizza')
#4-10  
first_three:list = nice_pizzas[:2 + 1]
print(f'The first three items in the list are {first_three}')
middle_three:list = nice_pizzas[3:5]
print(f'The middle two items in the list are {middle_three}')
last_three:list = nice_pizzas[5:]
print(f'The last two items in the list are {last_three}')