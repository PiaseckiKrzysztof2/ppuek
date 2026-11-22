# Zadanie 7-3.3 - Ile liczb parzystych (pętla while)
# Co robi: liczy, ile liczb parzystych jest w liście [34, 7, 19, 4, 21, 8], używając while.
#          Wynik: 3 (34, 4, 8).

numbers = [34, 7, 19, 4, 21, 8]

even_count = 0                                # schemat LICZNIKA
i = 0
while i < len(numbers):                       # i = 0, 1, ..., 5 (indeksy)
    if numbers[i] % 2 == 0:                   # parzysta
        even_count += 1
    i += 1

print('Array:', numbers)
print('Number of even values:', even_count)
