# Zadanie 9-5.8 - Koszt koszyka zakupów
# Co robi: dla każdego produktu w koszyku mnoży ilość przez cenę z cennika
#          i sumuje wszystko (3 x juice + 1 x bread + 2 x milk = 8.54).

prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

cart = {'juice': 3, 'bread': 1, 'milk': 2}

total = 0
for product, quantity in cart.items():
    total += prices[product] * quantity      # cenę bierzemy z drugiego słownika po tym samym kluczu

print(f'Total cost: {total:.2f}')
