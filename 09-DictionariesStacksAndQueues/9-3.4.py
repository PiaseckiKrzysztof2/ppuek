# Zadanie 9-3.4 - Zamiana liczby na dwójkową stosem
# Co robi: wczytuje liczbę naturalną i zamienia ją na zapis binarny: dzieli przez 2,
#          reszty kładzie na stos, a na koniec zdejmuje je w odwrotnej kolejności. 18 -> 10010.

import queue

number = int(input('Natural number: '))

remainders = queue.LifoQueue()
n = number
if n == 0:
    remainders.put(0)
while n > 0:
    remainders.put(n % 2)                    # reszta z dzielenia przez 2 (0 albo 1) na stos
    n = n // 2                               # dzielenie całkowite

binary = ''
while not remainders.empty():
    binary += str(remainders.get())          # stos oddaje reszty od OSTATNIEJ - dokładnie tak trzeba je czytać

print('Binary number:', binary)
