# Zadanie 7-3.6 - Maksimum i minimum bez max() i min()
# Co robi: znajduje największą i najmniejszą liczbę w liście [-15, 8, -31, 47, -2, 19]
#          samodzielnie, pętlą (bez funkcji wbudowanych). Wynik: 47 i -31.

numbers = [-15, 8, -31, 47, -2, 19]

maximum = numbers[0]                          # start od pierwszego elementu
minimum = numbers[0]
for n in numbers:
    if n > maximum:                           # schemat MAX: większy -> nowe maksimum
        maximum = n
    if n < minimum:                           # schemat MIN: mniejszy -> nowe minimum
        minimum = n

print('Array:', numbers)
print('Maximum:', maximum)
print('Minimum:', minimum)
