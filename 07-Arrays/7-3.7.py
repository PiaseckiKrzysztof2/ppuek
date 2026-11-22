# Zadanie 7-3.7 - Średnia (pętla for)
# Co robi: liczy średnią arytmetyczną liczb z listy [15, 8, 31, 47, 2, 19] pętlą for
#          i wypisuje listę oraz średnią (20.33).

numbers = [15, 8, 31, 47, 2, 19]

total = 0                                     # schemat SUMY
for n in numbers:
    total += n
mean = total / len(numbers)                   # średnia = suma / liczba elementów

print('Array:', numbers)
print(f'Arithmetic mean: {mean:.2f}')
