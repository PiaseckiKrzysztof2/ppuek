# Zadanie 9-1.2 - Podstawowe operacje na słowniku
# Co robi: pokazuje przykłady z treści zadania: tworzenie słownika, odczyt, dodawanie,
#          zmiana i usuwanie wartości, pętle po kluczach/wartościach i sprawdzanie klucza.

# Słownik = pary klucz: wartość w nawiasach { }
student = {
    'name': 'John',
    'age': 22,
    'major': 'Computer Science'
}

print(student['name'])                       # odczyt wartości przez KLUCZ (a nie indeks)

student['grade'] = 'A'                       # nowy klucz -> dodanie pary
student['age'] = 23                          # istniejący klucz -> zmiana wartości
del student['major']                         # del - usunięcie pary
print(student)

fruits = {'apple': 3, 'banana': 5, 'orange': 2}

for fruit in fruits:                         # pętla po słowniku daje KLUCZE
    print(fruit)

for count in fruits.values():                # values() - same wartości
    print(count)

for fruit, count in fruits.items():          # items() - pary klucz, wartość
    print(f"The count of {fruit} is {count}")

person = {'name': 'Alice', 'age': 30}
if 'name' in person:                         # in - czy jest taki KLUCZ
    print("Name is present in the dictionary.")
else:
    print("Name is not present.")
