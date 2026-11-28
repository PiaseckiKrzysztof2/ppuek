# Zadanie 8-3.5 - Sprawdzanie loginu i hasła
# Co robi: wczytuje login i hasło z klawiatury i wyrażeniami regularnymi sprawdza wymagania:
#          login - min. 6 znaków, tylko małe litery;
#          hasło - min. 8 znaków, tylko litery, cyfry i podkreślnik _.

import re

username = input('Username: ')
password = input('Password: ')

username_pattern = r'^[a-z]{6,}$'            # ^ początek, $ koniec, [a-z] mała litera, {6,} co najmniej 6
password_pattern = r'^[A-Za-z0-9_]{8,}$'     # litery, cyfry lub _, co najmniej 8

username_match = re.match(username_pattern, username)    # match - zwraca dopasowanie albo None
password_match = re.match(password_pattern, password)

if username_match and password_match:        # None działa jak False
    print('Username and password are correct.')
else:
    if not username_match:
        print('Incorrect username: at least 6 characters, lowercase letters only.')
    if not password_match:
        print('Incorrect password: at least 8 characters, letters, digits and _ only.')
