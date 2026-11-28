# Zadanie 9-5.9 - Samochody z każdego województwa
# Co robi: czyta z province.csv, która litera oznacza które województwo, a z vehicle.txt
#          numery rejestracyjne. Liczy, ile aut jest z każdego województwa (po pierwszej literze).

provinces = {}                               # litera -> nazwa województwa
with open('province.csv', 'r', encoding='utf-8') as file:
    next(file)                               # pomiń pierwszą linijkę (nagłówek Letter,Name)
    for line in file:
        letter, name = line.strip().split(',')   # 'D,Dolnośląskie' -> 'D' i 'Dolnośląskie'
        provinces[letter] = name

counts = {}                                  # litera -> liczba aut
for letter in provinces:
    counts[letter] = 0

with open('vehicle.txt', 'r') as file:
    for line in file:
        first_letter = line.strip()[0]       # [0] - pierwsza litera numeru
        if first_letter in counts:
            counts[first_letter] += 1

for letter, name in provinces.items():
    print(f'{name}: {counts[letter]}')
