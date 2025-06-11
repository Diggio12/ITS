PATH: str = 'Lezione_15/example.txt'
mode: str = 'r'
encoding: str = 'utf-8'

file = open(PATH)

print(file)

output: str = file.read()
print(output)