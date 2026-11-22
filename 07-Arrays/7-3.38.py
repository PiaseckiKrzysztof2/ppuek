# Zadanie 7-3.38 - Tablica 2D na 1D
# Co robi: funkcja to_1d zamienia tablicę 2D na zwykłą listę (wszystkie wiersze po kolei).
#          Np. [[2, 3], [1, 5]] -> [2, 3, 1, 5].


def to_1d(array_2d):
    result = []
    for row in array_2d:                      # dla każdego wiersza...
        for value in row:                     # ...każdy element dopisz na koniec
            result.append(value)
    return result


arrays = [
    [[2, 3], [1, 5]],
    [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]],
    [[2, 1], [3, 5], [7, 4], [2, 6]],
]

for arr in arrays:
    print(arr, '->', to_1d(arr))
