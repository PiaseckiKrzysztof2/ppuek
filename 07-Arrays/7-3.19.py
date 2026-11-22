# Zadanie 7-3.19 - Ile razy wartość jest w krotce
# Co robi: wczytuje wartość z klawiatury i liczy, ile razy występuje w krotce
#          (50, 20, 40, 50, 30, 50). Dla 50 wynik to 3.

numbers = (50, 20, 40, 50, 30, 50)

print('Tuple:', ','.join(str(n) for n in numbers))
value = int(input('Value: '))

counter = 0                                   # schemat LICZNIKA
for n in numbers:
    if n == value:
        counter += 1                          # krócej: numbers.count(value)

print('Number of occurrences:', counter)
