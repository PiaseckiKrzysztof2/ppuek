# Zadanie 9-3.1 - Operacje na stosie
# Co robi: kładzie na stos liczby 2, 3, 7, 4, 1, 9, 8. Zdejmuje dwie ostatnie (8 i 9)
#          i wypisuje ich sumę (17), a potem pętlą while sumuje resztę stosu (17).

import queue

numbers = queue.LifoQueue()                  # LifoQueue - STOS: Last In, First Out (ostatni wchodzi, pierwszy wychodzi)

for n in [2, 3, 7, 4, 1, 9, 8]:
    numbers.put(n)                           # put - połóż na wierzch stosu

last = numbers.get()                         # get - zdejmij z wierzchu: 8
second_last = numbers.get()                  # potem 9
print('Sum of the last two numbers:', last + second_last)

total = 0
while not numbers.empty():                   # dopóki stos nie jest pusty
    total += numbers.get()                   # 1, 4, 7, 3, 2
print('Sum of the remaining numbers:', total)
