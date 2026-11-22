# Zadanie 7-3.5 - Kwadraty elementów
# Co robi: dla listy [8, 2, 5, 1, 9] liczy drugą potęgę każdego elementu
#          i wypisuje obie listy: 8 2 5 1 9 oraz 64 4 25 1 81.

numbers = [8, 2, 5, 1, 9]

squares = []                                  # pusta lista
for n in numbers:
    squares.append(n ** 2)                    # ** - potęga; append - dopisz na koniec listy

print('Array:', ' '.join(str(n) for n in numbers))      # join - liczby oddzielone spacją
print('2nd power:', ' '.join(str(n) for n in squares))
