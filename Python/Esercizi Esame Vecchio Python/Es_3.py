def dict_prodotti(prodotti: dict[int | float]) -> dict:
    new_dict: dict = {}
    for key, value in prodotti.items():
        if value < 50:
            new_value = round((value +(value*10)/100), 2)
            new_dict[key] = [new_value]
    
    print(new_dict)


dict_prodotti({'Pane': 3.50, 'Zucchine':50, 'Lombata':120, 'Pepe':7.93})