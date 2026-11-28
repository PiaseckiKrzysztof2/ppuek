# Zadanie 8-4.8 - Pliki z 4-literowym rozszerzeniem
# Co robi: z listy nazw plików w files.txt wypisuje tylko te, których rozszerzenie
#          ma dokładnie 4 znaki (np. .html, .docx, .xlsx).

import re

with open('files.txt', 'r') as file:
    for line in file:
        name = line.strip()                  # strip - usuwa spacje i \n z początku i końca
        if re.search(r'\.\w{4}$', name):     # \. - kropka, \w{4} - 4 znaki, $ - koniec nazwy
            print(name)
