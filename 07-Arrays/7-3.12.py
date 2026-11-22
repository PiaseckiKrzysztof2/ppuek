# Zadanie 7-3.12 - Liczby, których nie ma w drugiej tablicy
# Co robi: wypisuje liczby z pierwszej listy, które nie występują w drugiej.
#          Wynik: 4 12 28 9 44.

first = [4, 36, 12, 28, 9, 44, 5]
second = [5, 1, 36]

print('First array:', first)
print('Second array:', second)
print('Numbers from the first array not in the second:', end=' ')
for n in first:
    if n not in second:                       # not in - czy elementu NIE MA w liście
        print(n, end=' ')
print()
