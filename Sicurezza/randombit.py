import sys
import random

if len(sys.argv) !=2:
    print(f'Usage: {sys.argv[0]} <file name')

data = None

with open (sys.argv[1], 'rb') as f:
    data = f.read()

pos = random.randint(0, len(data) -1)

bit = random.randint(0, 7)

byte = data[pos]

byte = byte ^ (1 << bit)

data = data[:pos] + bytes([byte]) + data[pos+1:]

with open(sys.argv[1], 'wb') as f:
    f.write(data)

print(f'Modificato il bit {bit} al posto {pos} nel file: {sys.argv[1]}')
