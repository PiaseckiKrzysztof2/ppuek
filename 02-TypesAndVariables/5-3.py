a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
volume = a * b * c
surface_area = 2 * (a*b + a*c + b*c)     # Oblicza pole powierzchni
print(f'Volume: {volume}')               # Wyświetla objętość
print(f'Surface area: {surface_area}')