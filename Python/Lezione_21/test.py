from Es_01 import *


e:Email = Email('Ciao Valerio come stai? Spero ti siano passate le turbe giovanili','Mattia', 'Valerio', 'Turbe Giovanili')
f:File = File('Python/Lezione_21/document.txt')

print(e.getText())
print(f.getText())

e.write_to_file('Python/Lezione_21/email1.txt')

print(e.isintext('incontrarci'))
print(e.isintext('percorso'))