# Zadanie 7-3.18 - Zagnieżdżona krotka
# Co robi: z krotki ("Seven", [10, 20, 30], (5, 15, 25)) wypisuje "Seven" i liczbę 30.

data = ("Seven", [10, 20, 30], (5, 15, 25))

print(data[0])                                # pierwszy element: "Seven"
print(data[1][2])                             # data[1] to lista [10, 20, 30], a [2] to jej trzeci element: 30
