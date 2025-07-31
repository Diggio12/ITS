frase = ('Nel mezzo del cammin di nostra vita')
list_1 = []
list_2 = []
list_3 = []
for i in frase:
    list_1.append(ord(i))
for c in list_1:
    list_2.append(c ^ 57)
for x in list_2:
    list_3.append(chr(57^x))

print(list_1, list_2, list_3)
    
