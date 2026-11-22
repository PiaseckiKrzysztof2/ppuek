# Zadanie 7-3.4 - Tablica od tyłu
# Co robi: wypisuje listę [15, 8, 31, 47, 2, 19] normalnie, a potem w odwrotnej kolejności.

numbers = [15, 8, 31, 47, 2, 19]

print('existed array:', end=' ')
for n in numbers:
    print(n, end=' ')
print()

print('reverse array:', end=' ')
for i in range(len(numbers) - 1, -1, -1):     # od ostatniego indeksu (5) do 0, krok -1
    print(numbers[i], end=' ')
print()
