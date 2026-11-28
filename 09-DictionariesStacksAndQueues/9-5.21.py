# Zadanie 9-5.21 - Ulubiony film do JSON
# Co robi: tworzy słownik z 5 informacjami o ulubionym filmie i zapisuje go
#          do pliku favourite.json.

import json

favourite = {
    "title": "Interstellar",
    "director": "Christopher Nolan",
    "year": 2014,
    "genre": "Science Fiction",
    "rating": 8.7
}

with open('favourite.json', 'w', encoding='utf-8') as file:
    json.dump(favourite, file, indent=4)     # słownik -> plik JSON

print('Saved to favourite.json')
