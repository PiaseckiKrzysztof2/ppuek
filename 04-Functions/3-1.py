# Funkcje i stałe z modułu math
# żeby użyć funkcji z math trzeba zaimportować moduł
import math

square_root = math.sqrt(7)
print('A square root of 7 is', square_root)

natural_log = math.log(5)  # log bez podstawy to logarytm naturalny
print('A natural logarithm of 5 is', natural_log)

# sin przyjmuje radiany, więc zamieniam stopnie
sine = math.sin(math.radians(90))
print('A sine of 90 degrees is', sine)
