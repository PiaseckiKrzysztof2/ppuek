# Zadanie 8-2.5 - Lista zakupów z klawiatury
# Co robi: wczytuje z klawiatury nazwy produktów, aż użytkownik wpisze 0.
#          Każdy produkt dopisuje na koniec pliku shopping_list.txt.

shopping_list = 'shopping_list.txt'


def add_product(file_name, product_name):
    with open(file_name, 'a') as file:       # 'a' - tryb dopisywania (append): dopisuje na KOŃCU, nie kasuje
        file.write(product_name + '\n')


product = ""
while product != "0":
    product = input('Enter product name (0 stops): ')
    if product == '0':
        break                                # break - natychmiast wychodzi z pętli
    else:
        add_product(shopping_list, product)

print(f'Shopping list saved in {shopping_list}.')
