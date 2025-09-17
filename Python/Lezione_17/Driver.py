from dottore import Dottore
from paziente import Paziente
from persona import Persona
from fatture import Fattura

doc1: Dottore = Dottore('Francesco', 'Virgolini', 'Osteopata', 12.9)
doc2:Dottore = Dottore('Mario', 'Rossi', 'Ginecologo', 9.6)

paz1: Paziente = Paziente('Giulio', 'Rossi', '69')
paz2: Paziente = Paziente('Giacomo', 'Testarossa', '12345')
paz3: Paziente = Paziente('Luca', 'Blicky', '6767')
paz4: Paziente = Paziente('Primo', 'Terzo', '13')

pazienti1: list[Paziente] = [paz1, paz2, paz3]
pazienti2: list[Paziente] = [paz4]

doc1.setAge(34)
doc2.setAge(69)

doc1.doctorGreet()
doc2.doctorGreet()

fattura1: Fattura = Fattura(pazienti1, doc1)
fattura2: Fattura = Fattura(pazienti2, doc2)

print(f'Salario {doc1}: {fattura1.getSalary()} euro!')
print(f'Salario {doc2}: {fattura2.getSalary()} euro!')

fattura1.removePatient('12345')
fattura2.addPatient('12345')

print(f'Salario {doc1}: {fattura1.getSalary()} euro!')
print(f'Salario {doc2}: {fattura2.getSalary()} euro!')

