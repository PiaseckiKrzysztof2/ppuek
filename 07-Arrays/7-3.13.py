# Zadanie 7-3.13 - Bubble sort na trzech tablicach
# Co robi: funkcja bubblesort sortuje listę rosnąco metodą bąbelkową
#          (jak w 7-1.15). Program sortuje i wypisuje trzy listy: przed i po.


def bubblesort(array):
    array = array.copy()
    n = len(array)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:                       # lewy większy od prawego
                array[j], array[j + 1] = array[j + 1], array[j]   # zamiana miejscami
                swapped = True
        if not swapped:                                       # nie było zamiany -> już posortowane, kończymy
            break
    return array


arrays = [
    [64, 34, 25, 12, 22, 11, 90],
    [5, -1, 3, 0, -8, 2],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

for arr in arrays:
    print('Before:', arr)
    print('After: ', bubblesort(arr))
    print()
