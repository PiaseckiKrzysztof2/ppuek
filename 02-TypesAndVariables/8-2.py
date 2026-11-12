# Calculation of circle area and circumference
r = float(input('Enter radius: '))             # Pobiera promień koła
pi = 3.14                                      # Wartość liczby PI
area = pi * r ** 2                             # Oblicza pole koła
circumference = 2 * pi * r                     # Oblicza obwód koła
print(f'Area: {area:.2f}')                     # Wyświetla pole koła
print(f'Circumference: {circumference:.2f}')   # Wyświetla obwód koła