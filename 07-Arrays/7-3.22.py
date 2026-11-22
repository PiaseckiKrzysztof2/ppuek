# Zadanie 7-3.22 - Najpierw parzyste, potem nieparzyste
# Co robi: układa liczby tak, żeby najpierw były parzyste, a potem nieparzyste.
#          [7, 9, 2, 4, 5, 6] -> [2, 4, 6, 7, 9, 5].

arr = [7, 9, 2, 4, 5, 6]
print('arr =', arr)

even = []
odd = []
for n in arr:
    if n % 2 == 0:                            # parzysta -> do listy even
        even.append(n)
    else:                                     # nieparzysta -> do listy odd
        odd.append(n)

arr = even + odd                              # + skleja dwie listy w jedną
print('arr =', arr)
