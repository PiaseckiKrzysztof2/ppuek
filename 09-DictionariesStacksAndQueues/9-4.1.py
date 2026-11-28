# Zadanie 9-4.1 - Przykład kolejki (queue_example.py)
# Co robi: tworzy kolejkę osób (Michael, Charlotte, Olivia) i obsługuje je po kolei.
#          Kto pierwszy wszedł, ten pierwszy wychodzi. To gotowy przykład z repo.

import queue

people = queue.Queue()                       # Queue - KOLEJKA: First In, First Out (pierwszy wchodzi, pierwszy wychodzi)

people.put('Michael')                        # put - dodaj na KONIEC kolejki
people.put('Charlotte')
people.put('Olivia')

print('Number of queue elements:', people.qsize())   # qsize - ile elementów

while not people.empty():
    person = people.get()                    # get - weź z POCZĄTKU kolejki
    print(person)
