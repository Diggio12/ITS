def sum_primary_diagonal(matrix: list[list[int]]) -> int:

    somma_diagonale_primaria: int = 0
    position: int = 0

    for lista in matrix:
        somma_diagonale_primaria += lista[position]
        position += 1

    print (somma_diagonale_primaria)
    return somma_diagonale_primaria

def sum_secondary_diagonal(matrix: list[list[int]]) -> int:

    somma_diagonale_secondaria: int = 0
    position: int = len(matrix) - 1

    for lista in matrix:
        somma_diagonale_secondaria += lista[position]
        position -= 1

    print (somma_diagonale_secondaria)
    return somma_diagonale_secondaria

sum_primary_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sum_secondary_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

