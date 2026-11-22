# Zadanie 7-3.26 - Odcinek na wykresie (matplotlib)
# Co robi: rysuje na wykresie odcinek od punktu (1, 3) do punktu (8, 10).
#          Wymaga biblioteki matplotlib: py -m pip install matplotlib

import matplotlib.pyplot as plt               # "as plt" - krótsza nazwa modułu

xpoints = [1, 8]                              # współrzędne x punktów
ypoints = [3, 10]                             # współrzędne y punktów

plt.plot(xpoints, ypoints)                    # rysuje linię przez punkty
plt.show()                                    # pokazuje okno z wykresem
