# Zadanie 8-4.10 - Tanie ubrania z małym stanem
# Co robi: czyta plik clothing.csv i wypisuje produkty, które kosztują mniej niż 60
#          i jest ich w magazynie mniej niż 40 sztuk.

import csv

with open('clothing.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        price = float(row['Price'])          # z pliku CSV wszystko jest NAPISEM -> zamiana na liczbę
        stock = int(row['Stock_Quantity'])
        if price < 60 and stock < 40:        # oba warunki naraz
            print(f"{row['Product_Name']} {row['Size']} {row['Color']}: price {price}, stock {stock}")
