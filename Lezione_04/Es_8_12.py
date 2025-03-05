sandwich_ingredients:list = ['tonno', 'pomodoro', 'prosciutto', 'rucola']
ingrediente_chosen:list = []
def sandwich_maker():
    i = 0
    while i < len(sandwich_ingredients):
        scelta = input(f'Aggiungere {sandwich_ingredients[i]} al panino? ')
        if scelta == 'si':
            ingrediente_chosen.append(sandwich_ingredients[i])
            i += 1
        elif scelta == 'no':
            i += 1
            continue
        else:
            print('comando non riconosciuto')
            continue

sandwich_maker()
print(f'Ingredienti aggiunti sul panino sono {ingrediente_chosen}')

