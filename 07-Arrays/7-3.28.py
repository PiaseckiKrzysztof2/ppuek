# Zadanie 7-3.28 - Wykres sinusa
# Co robi: rysuje wykres y = sin(x) dla kątów od 0 do 360 stopni. Wymaga matplotlib.

import math
import matplotlib.pyplot as plt

x = []
y = []
for degrees in range(0, 361):
    x.append(degrees)
    y.append(math.sin(math.radians(degrees)))     # sin przyjmuje radiany -> radians()

plt.plot(x, y)
plt.title('y = sin(x)')
plt.xlabel('x [degrees]')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()
