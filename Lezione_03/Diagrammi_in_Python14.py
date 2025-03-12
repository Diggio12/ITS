punteggio:int = 0
somma_tiro_dadi:int = 0

while True:
    lancio_D1:int = int(input('Inserire valore lancio primo dado: '))
    lancio_D2:int = int(input('Inserire valore lancio secondo dado: '))
    if lancio_D1 <= 6 and lancio_D1 >= 1 and lancio_D2 <= 6 and lancio_D2 >= 1:
        somma_tiro_dadi = somma_tiro_dadi + (lancio_D1 + lancio_D2)
        if lancio_D1 % 2 == 0 and lancio_D2 % 2 == 0 and somma_tiro_dadi >= 8:
            punteggio = 100
            print('Hai vinto!', punteggio)
            break
        elif lancio_D1 == 6 or lancio_D2 == 6 and somma_tiro_dadi == 7:
            punteggio += 10
            if punteggio >= 100:
                print('Hai vinto')
                break

        else:
            punteggio = 0
            print('Hai perso', punteggio)
            break
    else:
        print('Valori lancio dadi non possibili')

