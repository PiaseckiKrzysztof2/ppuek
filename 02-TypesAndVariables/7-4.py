import math                                                       # Import modułu matematycznego
circumference = float(input('Enter tree circumference in cm: '))  # Pobiera obwód drzewa
diameter = circumference / math.pi                                # Oblicza średnicę drzewa (math.pi / ~3.14 liczba π)
can_cut = diameter >= 50
print(f'Tree can be cut down: {can_cut}')