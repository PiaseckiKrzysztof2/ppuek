# Zadanie 7-3.20 - Moduł MyArrays
# Co robi: MODUŁ z funkcjami na liście liczb: liczba elementów, najmniejsza i największa,
#          druga co do wielkości, różnica max-min, mediana i lista jako napis z myślnikami.
#          Zgodnie z treścią NIE używa len, max, min, sorted, sum - wszystko pętlami.


def count(array):
    n = 0
    for _ in array:                           # "_" - zmienna, której nie używamy
        n += 1
    return n


def smallest_largest(array):
    smallest = array[0]
    largest = array[0]
    for x in array:
        if x < smallest:
            smallest = x
        if x > largest:
            largest = x
    return [smallest, largest]                # zwraca dwuelementową listę


def second_largest(array):
    largest = smallest_largest(array)[1]
    second = None
    for x in array:
        if x < largest and (second is None or x > second):   # największa z tych mniejszych od max
            second = x
    return second


def difference(array):
    pair = smallest_largest(array)
    return pair[1] - pair[0]


def sort_array(array):
    result = []
    for x in array:
        result += [x]
    n = count(result)
    for i in range(n - 1):                    # bubble sort
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def median(array):
    ordered = sort_array(array)               # mediana = środek POSORTOWANEJ listy
    n = count(ordered)
    middle = n // 2
    if n % 2 == 1:                            # nieparzysta liczba elementów -> środkowy
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2   # parzysta -> średnia dwóch środkowych


def to_string(array, separator='-'):
    result = ''
    first = True
    for x in array:
        if not first:
            result += separator
        result += str(x)
        first = False
    return result


if __name__ == "__main__":
    print(second_largest([7, 3, 8, 5, 2]))
    print(median([7, 3, 8, 5, 2]), median([1, 2, 3, 4]))
