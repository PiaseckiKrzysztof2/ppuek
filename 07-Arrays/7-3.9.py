# Zadanie 7-3.9 - Najdłuższe imię
# Co robi: z listy imion wypisuje to, które ma najwięcej liter (Celestyna).

names = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

longest = names[0]
for name in names:
    if len(name) > len(longest):              # schemat MAX, ale porównujemy DŁUGOŚCI
        longest = name

print('Names:', ' '.join(names))
print('Longest name:', longest)
