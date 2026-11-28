# Zadanie 9-1.7 - Produkty w sklepie komputerowym
# Co robi: wypisuje listę produktów z ich ilością i liczy, ile produktów jest
#          w sklepie razem (330).

products = {
    'Laptop': 15,
    'Desktop PC': 10,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60,
    'External Hard Drive': 30,
    'Printer': 12,
    'Router': 20,
    'USB Flash Drive': 100,
    'Graphics Card': 8
}

total = 0                                    # schemat SUMY
for product, quantity in products.items():
    print(f'{product}: {quantity}')
    total += quantity

print('Total number of products:', total)
