# Zadanie 7-3.32 - Tabliczka mnożenia
# Co robi: wypełnia tablicę 5x5 (z zer) tabliczką mnożenia 1-5 i ją wypisuje.

array = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

for r in range(len(array)):                   # r - numer wiersza
    for c in range(len(array[r])):            # c - numer kolumny
        array[r][c] = (r + 1) * (c + 1)       # + 1, bo indeksy są od 0, a mnożymy od 1

for row in array:
    for value in row:
        print(f'{value:3}', end='')
    print()
