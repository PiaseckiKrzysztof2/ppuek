# Zadanie 7-3.27 - Wykres funkcji f(x) = x^2 - 3
# Co robi: tworzy listę x od -100 do 100, liczy dla każdego y = x^2 - 3
#          i rysuje wykres (parabola). Wymaga matplotlib.

import matplotlib.pyplot as plt

x = []
y = []

for n in range(-100, 101):                    # 101, żeby 100 też weszło
    x = x + [n]

for n in x:
    y = y + [n ** 2 - 3]                      # wartość funkcji dla każdego x

plt.plot(x, y)
plt.title('f(x) = x^2 - 3')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
