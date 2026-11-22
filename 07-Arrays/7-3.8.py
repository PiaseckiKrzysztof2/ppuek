# Zadanie 7-3.8 - Średnia (pętla while)
# Co robi: to samo co 7-3.7, ale pętlą while: liczy średnią z [15, 8, 31, 47, 2, 19] (20.33).

numbers = [15, 8, 31, 47, 2, 19]

total = 0
i = 0
while i < len(numbers):                       # dopóki są elementy
    total += numbers[i]
    i += 1                                    # następny indeks
mean = total / len(numbers)

print('Array:', numbers)
print(f'Arithmetic mean: {mean:.2f}')
