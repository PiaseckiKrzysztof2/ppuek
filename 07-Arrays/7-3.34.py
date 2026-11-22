# Zadanie 7-3.34 - Zamiana wierszy
# Co robi: w tablicy 3x5 zamienia miejscami pierwszy i ostatni wiersz.
#          Wypisuje tablicę przed i po zmianie.


def print_2d(array):
    for row in array:
        for value in row:
            print(f'{value:4}', end='')
        print()


array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print('Before:')
print_2d(array)

array[0], array[-1] = array[-1], array[0]     # swap: pierwszy wiersz <-> ostatni wiersz

print('After:')
print_2d(array)
