people_for_dinner:list =  ["Churchill", "Fermi", "Napoleone"]
print(f"Je suis désolée about the fact that tonight you will not be join us {people_for_dinner[2]}")
people_for_dinner.pop(2)
people_for_dinner.insert(2, "Lebron")
for people in people_for_dinner:
    print (f'Hello {people} I would like to invite you to dinner')
