# Zadanie 9-5.5 - Ile razy występuje każde słowo
# Co robi: liczy w zdaniu, ile razy pojawia się każde słowo, i zapisuje to w słowniku
#          słowo: liczba (cat 3, dog 1, mouse 2, rat 1).

paragraph = "cat dog mouse cat rat cat mouse"

word_count = {}                              # pusty słownik
for word in paragraph.split():               # split - lista słów
    if word in word_count:
        word_count[word] += 1                # słowo już było -> zwiększ o 1
    else:
        word_count[word] = 1                 # nowe słowo -> zaczynamy od 1

for word, count in word_count.items():
    print(f'{word}: {count}')
