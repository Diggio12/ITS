def merge_intervals(intervals: list[list[int]]):

    lista_nuova_intervalli: list = []

    for intervalli in intervals:
        intervallo_minore: int = 0
        intervallo_maggiore: int = 0
        if intervalli[0] > intervallo_minore:
           
           intervallo_minore = intervalli[0]

           lista_nuova_intervalli.append(intervallo_minore)

        elif intervalli[-1] > intervallo_maggiore:

            intervallo_maggiore = intervalli[-1]

            lista_nuova_intervalli.append(intervallo_maggiore)
           