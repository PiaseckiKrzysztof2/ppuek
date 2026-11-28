# Zadanie 9-5.22 - Produkt z klawiatury do JSON
# Co robi: wczytuje z klawiatury nazwę produktu, cenę i to, czy jest opłacony (yes/no),
#          zamienia je na właściwe typy (str, float, bool) i zapisuje do product.json.

import json

product = {}

product['name'] = input('Product name: ')
product['price'] = round(float(input('Price: ')), 2)        # float - liczba z kropką, 2 miejsca
product['paid'] = input('Paid (yes/no): ').lower() == 'yes'  # porównanie daje True/False

with open('product.json', 'w', encoding='utf-8') as file:
    json.dump(product, file, indent=4)

print('Saved to product.json:', product)
