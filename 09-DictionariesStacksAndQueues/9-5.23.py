# Zadanie 9-5.23 - Kursy euro z NBP
# Co robi: wczytuje plik euro.json z 10 ostatnimi kursami euro pobranymi z api.nbp.pl
#          i wypisuje tabelkę: data, kurs kupna, kurs sprzedaży.
#          Plik euro.json pobrano z adresu:
#          https://api.nbp.pl/api/exchangerates/rates/C/EUR/last/10/?format=json

import json

with open('euro.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print(f"{'Date':<16}{'Buying Rate':<16}Selling Rate")
print('=' * 44)
for rate in data['rates']:                   # 'rates' - lista słowników z kursami
    print(f"{rate['effectiveDate']:<16}{rate['bid']:<16.4f}{rate['ask']:.4f}")   # bid - kupno, ask - sprzedaż
