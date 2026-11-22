# Zadanie 7-3.37 - Transpozycja macierzy
# Co robi: funkcja transpose_matrix zamienia wiersze z kolumnami (pierwszy wiersz
#          staje się pierwszą kolumną itd.). Program wypisuje 3 macierze przed i po.


def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])
    result = []
    for c in range(cols):                     # każda kolumna staje się nowym wierszem
        new_row = []
        for r in range(rows):
            new_row.append(m[r][c])           # element [r][c] trafia na [c][r]
        result.append(new_row)
    return result


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(value) for value in row))


matrices = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]],
    [[5, 6, 7, 8]],
]

for m in matrices:
    print('Matrix:')
    print_matrix(m)
    print('Transposed:')
    print_matrix(transpose_matrix(m))
    print()
