# Zadanie 7-3.30 - Suma ostatniej kolumny
# Co robi: liczy sumę liczb w ostatniej kolumnie tablicy 2D (0 + 5 + 7 + 5 = 17).

array = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

total = 0
for row in array:
    total += row[-1]                          # row[-1] - ostatni element wiersza = ostatnia kolumna

print('Sum of values in the last column:', total)
