# Zadanie 9-5.6 - Połączenie dwóch słowników
# Co robi: tworzy słownik person, który zawiera wszystkie dane z basic_data
#          i advanced_data (razem 5 par), i go wypisuje.

basic_data = {
    "name": "Barbara",
    "age": 21
}

advanced_data = {
    "status": "student",
    "married": False,
    "interest": ["reading", "swimming"]
}

person = {}
person.update(basic_data)                    # update - dopisuje wszystkie pary z innego słownika
person.update(advanced_data)

print(person)
