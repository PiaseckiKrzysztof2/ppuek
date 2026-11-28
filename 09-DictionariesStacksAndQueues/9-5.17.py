# Zadanie 9-5.17 - Miasta z pliku JSON
# Co robi: wczytuje plik cities.json (lista słowników - jeden na miasto) i wypisuje
#          dane każdego miasta, z pustą linijką między miastami.

import json

with open('cities.json', 'r', encoding='utf-8') as file:    # utf-8 - polskie znaki w nazwach miast
    data = json.load(file)                   # JSON -> lista słowników

for city in data:                            # każde miasto to słownik
    for key, value in city.items():
        print(key, ':', value)
    print()
