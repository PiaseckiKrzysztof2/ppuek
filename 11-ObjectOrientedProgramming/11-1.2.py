# Zadanie 11-1.2 - Klasa Square (kwadrat)
# Co robi: klasa Square ma bok a i metody liczące pole i (dodany) obwód.
#          Program tworzy kwadraty o boku 4 i 6 i wypisuje ich pola i obwody.


class Square:
    def __init__(self, a):                   # a podajemy przy tworzeniu: Square(4)
        self.a = a

    def area(self):                          # METODA - funkcja w klasie; self = ten konkretny obiekt
        return self.a * self.a

    def perimeter(self):                     # dodana metoda: obwód = 4 * bok
        return 4 * self.a


square1 = Square(4)
square2 = Square(6)

print('Square with side 4:')
print(f'Area is {square1.area()}, Perimeter is {square1.perimeter()}')    # obiekt.metoda()
print('Square with side 6:')
print(f'Area is {square2.area()}, Perimeter is {square2.perimeter()}')
