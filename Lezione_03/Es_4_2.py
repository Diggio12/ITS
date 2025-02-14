cool_animals:list = ['Dog', 'Cat', 'Parrot']
for animals in cool_animals:
    #print(animals)        #basic print of the name of each animal
    print(f'A {animals} would make a great pet')

i = 0

while i < len(cool_animals):
    print(f"A {cool_animals[i]} would make a great pet")
    i += 1
    
print(f'A {cool_animals[0]}, a {cool_animals[1]} and {cool_animals[2]}, have in common the fact that they are domestic animals.\n But they all are great pets!')
