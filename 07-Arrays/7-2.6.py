# Zadanie 7-2.6 - Przekątna macierzy
# Co robi: w macierzy 3x3 z samych zer wstawia 1 na głównej przekątnej
#          (lewy górny -> prawy dolny róg) i wypisuje wynik.

matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(matrix)):
    matrix[i][i] = 1              # przekątna: numer wiersza == numer kolumny

for row in matrix:
    for value in row:
        print(value, end=' ')
    print()
