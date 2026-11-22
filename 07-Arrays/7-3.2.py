# Zadanie 7-3.2 - Tworzenie różnych tablic
# Co robi: tworzy 14 różnych list (zwykłe, 2D, wypełnione liczbami, losowe, zerami, False)
#          i wypisuje każdą z nich. Większość tworzona jest skrótem "list comprehension".

import random

arr1 = [3, 7, 1, 0, 4]
arr2 = [[2, 3], [7, 1], [0, 4]]                                      # lista 2D (lista list)
arr3 = [7 for i in range(5)]                                         # [wartość for ... in ...] - list comprehension
arr4 = [i for i in range(1, 10)]                                     # 1..9
arr5 = [i * 2 for i in range(1, 10)]                                 # 2, 4, ..., 18
arr6 = [random.randint(1, 20) for i in range(10)]                    # 10 losowych liczb
arr7 = [[] for i in range(5)]                                        # 5 pustych list
arr8 = [[1 for i in range(2)] for j in range(4)]                     # 4 wiersze x 2 kolumny jedynek
arr9 = [[random.randint(1, 20) for i in range(3)] for j in range(5)]

arr10 = [4, 0, 3]
arr11 = [0] * 15                                                     # 15 zer
arr12 = list(range(1, 31))                                           # liczby 1..30
arr13 = [random.randint(0, 1) for i in range(20)]                    # 20 losowych 0/1
arr14 = [[False for c in range(2)] for r in range(5)]                # 5 wierszy x 2 kolumny False

all_arrays = [arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9,
              arr10, arr11, arr12, arr13, arr14]

for number, arr in enumerate(all_arrays, start=1):                   # enumerate - numer i element naraz
    print(f'arr{number} =', arr)
