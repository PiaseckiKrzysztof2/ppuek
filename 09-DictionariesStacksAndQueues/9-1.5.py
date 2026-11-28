# Zadanie 9-1.5 - Lista słowników z krajami
# Co robi: tworzy listę 5 słowników (kraj i liczba ludności) i wypisuje ją jako tabelkę
#          z kolumnami COUNTRY i POPULATION.

countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83200000},
    {"name": "France", "population": 67800000},
    {"name": "Spain", "population": 47400000},
    {"name": "Italy", "population": 58900000}
]

print(f"{'COUNTRY':<9}POPULATION")           # :<9 - wyrównaj do lewej na 9 znakach
for country in countries:                    # każdy element listy to słownik
    print(f"{country['name']:<9}{country['population']}")
