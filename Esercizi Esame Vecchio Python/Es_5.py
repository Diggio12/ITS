def moltiplicatore(lista_numeri: list[int | float]) -> int:
    moltiplicazione = 1
    for i in lista_numeri:
        if i % 1 == 0 and i < 62:
            moltiplicazione *= i
    
    print (moltiplicazione)

moltiplicatore([3, 65.5, 8.439, 21, 120, 5, 17.34])