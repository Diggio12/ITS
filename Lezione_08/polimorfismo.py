from persona import Persona
from alieno import Alieno

p: Persona = Persona('Mattia', 'Di Giorgio', 21)

print(p)

et: Alieno = Alieno('Andromeda')

print(et)

p.speak()

et.speak()