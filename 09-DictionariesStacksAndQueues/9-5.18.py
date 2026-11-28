# Zadanie 9-5.18 - Psy młodsze niż 5 lat
# Co robi: wczytuje dane psów z dogs.json i wypisuje tylko psy młodsze niż 5 lat.

import json

with open('dogs.json', 'r', encoding='utf-8') as file:
    dogs = json.load(file)

for dog in dogs:
    if dog['age'] < 5:                       # wiek z JSON jest już liczbą (int)
        print(f"{dog['name']} ({dog['breed']}), {dog['age']} years, owner: {dog['owner']}")
