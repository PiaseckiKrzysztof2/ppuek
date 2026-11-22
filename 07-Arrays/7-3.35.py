# Zadanie 7-3.35 - Zamiana kolumn
# Co robi: w tablicy 3x5 zamienia miejscami pierwszą i ostatnią kolumnę.
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

for row in array:                             # kolumna to nie osobna lista -> zamiana w KAŻDYM wierszu
    row[0], row[-1] = row[-1], row[0]

print('After:')
print_2d(array)
