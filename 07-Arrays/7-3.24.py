# Zadanie 7-3.24 - Losowy element tablicy
# Co robi: funkcja rand_elem zwraca losowy element listy. Program 5 razy
#          wypisuje losowy kolor z listy kolorów.

import random


def rand_elem(array):
    index = random.randint(0, len(array) - 1)     # losowy indeks od 0 do ostatniego
    return array[index]


colors = ['red', 'green', 'blue', 'yellow', 'black', 'white']
print('Array:', colors)
for i in range(5):
    print('Random element:', rand_elem(colors))
