numero_tutor:int = 10
attesa:int = 0

while True:

    studente:str = input('Inserire nome e cognome studente: ')
    if numero_tutor == 0 and attesa > 50:
        break
   
    else:
        if numero_tutor > 0:
            numero_tutor-= 1
            print(f'Tutor assegnato con successo allo studente {studente}')
    
        else:
            attesa += 1
            print('Studente in attesa che un tutor si liberi')