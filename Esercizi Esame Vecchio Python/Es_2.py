def ritorna_dict(lista_numeri: list) -> dict:
    my_dict: dict = {'Positivi': [], 'Negativi':[]}
    for i in lista_numeri:
        if i >= 0:
            my_dict['Positivi'] += [i]
        else:
            my_dict['Negativi'] += [i]

    print (my_dict)


ritorna_dict([3, 2, -65, 76, -12, 56, 86, 9])