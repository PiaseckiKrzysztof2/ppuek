# Zadanie 7-3.29 - Tablica 2x4
# Co robi: wypisuje tablicę 2D (2 wiersze, 4 kolumny) w równych wierszach i kolumnach.

array = [
    [3, 8, 1, 6],
    [9, 2, 7, 4]
]

for row in array:                             # pętla w pętli: wiersze, potem komórki
    for value in row:
        print(f'{value:3}', end='')           # :3 - każda liczba na 3 miejscach (równe kolumny)
    print()
