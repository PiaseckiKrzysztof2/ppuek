# Zadanie 9-1.4 - Operacje na słowniku person
# Co robi: na słowniku z danymi osoby: wypisuje imię i hobby, cały słownik, zmienia nazwisko
#          i stan cywilny, dodaje płeć, nowe hobby i telefon do pracy, a na koniec wypisuje całość.
# Typy wartości: name, surname - str; age - int; hobby - list; married - bool; phone - dict (słownik w słowniku).

person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {"landline": "123444321", "mobile": "777888999"}
}

print(person["name"])                        # 1. imię
print(person["hobby"])                       # 2. hobby
print(person)                                # 3. cały słownik

person["surname"] = "Nowak"                  # 4. zmiana nazwiska
person["married"] = not person["married"]    # 5. not odwraca True <-> False
person["gender"] = "male"                    # 6. nowy klucz
person["hobby"].append("bicycle")            # 7. hobby to lista -> append dopisuje
person["phone"]["work"] = "313131444"        # 8. słownik w słowniku: dwa klucze po kolei

for key, value in person.items():            # 9. cały słownik w pętli
    print(f"{key}: {value}")
