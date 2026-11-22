# Zadanie 7-3.11 - Porównanie tablic
# Co robi: funkcja compare zwraca True, jeśli dwie listy są takie same (ta sama długość
#          i te same elementy na tych samych pozycjach). Program porównuje 4 pary list.


def compare(array1, array2):
    if len(array1) != len(array2):            # różna długość -> na pewno różne
        return False
    for i in range(len(array1)):
        if array1[i] != array2[i]:            # różny element na tej samej pozycji
            return False
    return True


def to_text(array):
    return ' '.join(str(x) for x in array)


pairs = [
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2]),
]

for array1, array2 in pairs:
    print('Array1:', to_text(array1))
    print('Array2:', to_text(array2))
    if compare(array1, array2):
        print('Comparison: arrays are the same')
    else:
        print('Comparison: arrays are different')
    print()
