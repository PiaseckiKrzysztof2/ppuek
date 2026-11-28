# Zadanie 8-3.4 - Suma wydatków z e-maila
# Co robi: czyta e-mail z pliku report.txt, wyrażeniem regularnym znajduje wszystkie
#          kwoty zapisane jako €liczba i sumuje je (102 + 30 + 15 + 20 = 167).

import re

email_file = 'report.txt'

with open(email_file, 'r', encoding='utf-8') as file:    # utf-8, bo w pliku jest znak €
    email = file.read()

pattern = r'€(\d+)'                          # € i za nim cyfry; nawias () - zwróć tylko liczbę

amounts = re.findall(pattern, email)         # ['102', '30', '15', '20'] - to są NAPISY

total = 0
for amount in amounts:
    total += int(amount)                     # napis -> liczba

print(f'Total money spent: €{total}')
