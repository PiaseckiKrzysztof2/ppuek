# Zadanie 7-1.4 - Podstawy tablicy (listy)
# Co robi: dla listy [2, 3, 7, 5, 4] wypisuje: całą listę, liczbę elementów, pierwszy,
#          drugi, ostatni i przedostatni element, sumę pierwszego i ostatniego,
#          środkowy element, a na końcu wszystkie elementy pętlą, oddzielone spacją.

arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))                       # len - ile elementów
print('First value', arr[0])                                # indeksy liczymy od 0
print('Second value', arr[1])
print('Last value', arr[len(arr) - 1])                      # ostatni: len - 1 (5 elementów -> indeks 4)
print('Last but one value', arr[len(arr) - 2])              # przedostatni
print('Sum of the first and last value', arr[0] + arr[len(arr) - 1])
print('Middle value', arr[len(arr) // 2])                   # środek: 5 // 2 = 2

print('All values:', end=' ')
for value in arr:
    print(value, end=' ')                                   # end=' ' - wszystko w jednej linii
print()
