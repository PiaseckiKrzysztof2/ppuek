# Zadanie 7-1.12 - Najdroższa kategoria wydatków
# Co robi: są dwie listy - kategorie i wydatki (ten sam indeks = ta sama kategoria).
#          Program szuka największego wydatku i wypisuje jego kategorię (Rent, 1000).

categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

max_index = 0                                 # schemat MAX, ale zapamiętujemy INDEKS
for i in range(len(expenses)):                # pętla po indeksach: 0, 1, 2, 3
    if expenses[i] > expenses[max_index]:
        max_index = i

print(f'The most expensive category: {categories[max_index]} ({expenses[max_index]})')
