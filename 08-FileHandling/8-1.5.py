# Zadanie 8-1.5 - Ponumerowana lista krajów
# Co robi: czyta plik countries.txt linijka po linijce i wypisuje kraje z numerami:
#          1. Poland, Warsaw, 38265000   2. Germany, ...

number = 1                                   # licznik do numerowania
with open('countries.txt', 'r') as file:
    for line in file:
        print(f'{number}. {line}', end="")
        number += 1
print()
