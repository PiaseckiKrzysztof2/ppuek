# Pole trójkąta ze wzoru Herona
import math


def triangle_area(a, b, c):
    s = (a + b + c) / 2  # połowa obwodu
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # wzór Herona
    return area


# boki podane z klawiatury
a = float(input('Enter side a: '))
b = float(input('Enter side b: '))
c = float(input('Enter side c: '))
print(f'The area of a triangle with sides {a}, {b}, {c} is {triangle_area(a, b, c)}')

# sprawdzenie dla danych z zadania
print(f'The area of a triangle with sides 3, 4, 5 is {triangle_area(3, 4, 5)}')
print(f'The area of a triangle with sides 5, 12, 13 is {triangle_area(5, 12, 13)}')
print(f'The area of a triangle with sides 7, 24, 25 is {triangle_area(7, 24, 25)}')
