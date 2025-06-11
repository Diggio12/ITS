def even_odd_pattern(numbers: list[int]) -> list[int]:
    num_pari: list[int]= []
    num_disp: list[int]= []
    for i in numbers:
        if i % 2 == 0:
            num_pari.append(i)
        elif i % 2 == 1:
            num_disp.append(i)

    return num_pari + num_disp