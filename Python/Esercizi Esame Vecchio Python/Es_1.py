def conversione_tuple(lista_tuple: list[tuple]) -> dict:
    my_dict: dict = {}
    for key, value in lista_tuple:
        if key in my_dict:
            my_dict[key] += value
        else:
            my_dict[key] = value
    print(my_dict)

conversione_tuple([('marco', 4),('elisa', 5), ('marco', 2) ])

        
