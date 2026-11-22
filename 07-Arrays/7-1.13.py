# Zadanie 7-1.13 - Wartość towarów w sklepie
# Co robi: dla 10 produktów są ceny i ilości sztuk (ten sam indeks = ten sam produkt).
#          Program liczy wartość wszystkich towarów: suma (cena * ilość).

product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

total_value = 0                               # schemat SUMY
for i in range(len(product_prices)):
    total_value += product_prices[i] * product_quantities[i]   # cena * ilość dla tego samego i

print(f'Total value of goods in the store: {total_value:.2f}')  # :.2f - 2 miejsca po przecinku
