# Zadanie 7-3.14 - Elementy unikalne
# Co robi: wypisuje elementy, które występują w liście tylko raz.
#          Dla 2 3 2 5 8 1 9 8 wynik to 3 5 1 9.

array = [2, 3, 2, 5, 8, 1, 9, 8]

unique = []
for element in array:
    if array.count(element) == 1:             # .count - ile razy element jest w liście
        unique.append(element)

print('Array:', ' '.join(str(x) for x in array))
print('Unique elements:', ' '.join(str(x) for x in unique))
