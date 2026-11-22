# Zadanie 7-1.5 - Zmiana wartości w tablicy
# Co robi: zmienia elementy listy [1, 2, 3, 4, 5] i wypisuje ją po każdej zmianie:
#          od pierwszego odejmuje 1, do ostatniego dodaje 4, środkowy mnoży przez 2.

arr = [1, 2, 3, 4, 5]
print('Array:', arr)

arr[0] -= 1                       # listę można zmieniać: arr[indeks] = nowa wartość
print('Array:', arr)

arr[len(arr) - 1] += 4            # ostatni element + 4
print('Array:', arr)

arr[len(arr) // 2] *= 2           # środkowy element * 2
print('Array:', arr)
