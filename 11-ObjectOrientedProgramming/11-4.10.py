# Zadanie 11-4.10 - Punkty w pierwszej ćwiartce (klasa C)
# Co robi: klasa C dostaje listę punktów [x, y]. Metoda m(n) zwraca True, jeśli co najmniej
#          n punktów leży w pierwszej ćwiartce (x > 0 i y > 0). Dla przykładu: m(2) True, m(3) False.


class C:
    def __init__(self, points):
        self.points = points                 # lista 2D, np. [[2, 3], [1, 8], ...]

    def m(self, n):
        counter = 0                          # schemat LICZNIKA
        for x, y in self.points:             # każdy punkt rozpakowany na x i y
            if x > 0 and y > 0:
                counter += 1
        return counter >= n


obj = C([[2, 3], [1, 8], [-6, 4], [3, -7]])
print('m(2) returns', obj.m(2))
print('m(3) returns', obj.m(3))
