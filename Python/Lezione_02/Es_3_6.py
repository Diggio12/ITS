people_for_dinner:list =  ["Churchill", "Fermi", "Napoleone"]
print(f"Je suis désolée about the fact that tonight you will not be join us {people_for_dinner[2]}")
people_for_dinner.pop(2)
people_for_dinner.insert(2, "Lebron")
for people in people_for_dinner:
    print (f'Hello {people} I would like to invite you to dinner')

print(f"Good evening, {people_for_dinner[0]}, {people_for_dinner[1]}, {people_for_dinner[2]}. I have found a bigger dinner table for tonight")
people_for_dinner.insert(0, "Lincoln")
people_for_dinner.insert(1, "Curry")
people_for_dinner.append("Tom Brady")
for people in people_for_dinner:
    print (f'Hello {people} I would like to invite you to dinner')
