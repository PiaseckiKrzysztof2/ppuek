# Zadanie 8-4.9 - Moduł csv: graficy
# Co robi: modułem csv czyta plik it_company.csv i dla osób na stanowisku
#          'Graphic Designer' wypisuje: imię nazwisko,e-mail.

import csv

print('GRAPHIC DESIGNERS')
print('=================')

with open('it_company.csv', 'r') as file:
    reader = csv.DictReader(file)            # DictReader - każdy wiersz to SŁOWNIK z nazwami kolumn
    for row in reader:
        if row['Job Title'] == 'Graphic Designer':
            print(f"{row['First Name']} {row['Last Name']},{row['Email']}")
