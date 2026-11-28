# Zadanie 9-5.16 - Dane komputera z pliku JSON
# Co robi: wczytuje plik computer.json (jeden słownik) i wypisuje wszystkie
#          informacje o komputerze jako "klucz : wartość".

import json

with open('computer.json', 'r', encoding='utf-8') as file:
    data = json.load(file)                   # JSON -> słownik

for key, value in data.items():
    print(key, ':', value)
