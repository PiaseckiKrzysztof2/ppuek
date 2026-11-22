# Zadanie 7-3.23 - Czy podzbiór
# Co robi: funkcja is_subset sprawdza, czy wszystkie elementy pierwszej listy
#          są w drugiej liście. Program sprawdza 3 przykłady.


def is_subset(first, second):
    for element in first:
        if element not in second:             # brakuje choć jednego -> to nie podzbiór
            return False
    return True


tests = [
    ([1, 3, 5], [5, 4, 3, 2, 1]),
    ([1, 3, 7], [5, 4, 3, 2, 1]),
    ([], [1, 2]),
]

for first, second in tests:
    result = 'is' if is_subset(first, second) else 'is not'
    print(f'{first} {result} a subset of {second}')
