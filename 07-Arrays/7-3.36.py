# Zadanie 7-3.36 - Macierz jednostkowa
# Co robi: funkcja identity_matrix(n) tworzy macierz n x n z jedynkami na przekątnej
#          i zerami w pozostałych miejscach. Program wypisuje macierze 3x3, 5x5 i 8x8.


def identity_matrix(n):
    matrix = []
    for r in range(n):
        row = []
        for c in range(n):
            row.append(1 if r == c else 0)    # przekątna (r == c) -> 1, reszta -> 0
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(value) for value in row))


for size in [3, 5, 8]:
    print(f'Identity matrix {size}x{size}:')
    print_matrix(identity_matrix(size))
    print()
