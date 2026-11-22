# Zadanie 7-3.10 - Wykres z gwiazdek
# Co robi: funkcja star(n) zwraca n gwiazdek. Program dla każdej liczby z listy
#          wypisuje ją i tyle gwiazdek, ile wynosi, np. "4: ****".


def star(n):
    return '*' * n                            # napis * liczba -> powtórzenie napisu


numbers = [2, 6, 4, 9, 7]
for n in numbers:
    print(f'{n}: {star(n)}')
