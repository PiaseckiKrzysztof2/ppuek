# Zadanie 9-5.11 - Głosowanie zapisywane w pliku JSON
# Co robi: wczytuje wyniki z voting.json, pyta, na kogo głosujesz, i dodaje tej osobie
#          1 głos (nowa osoba dostaje 1). Zapisuje wyniki z powrotem do pliku.
#          Można uruchamiać wiele razy - głosy się sumują.

import json

file_name = 'voting.json'

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        votes = json.load(file)              # json.load - zamienia plik JSON na słownik Pythona
except FileNotFoundError:
    votes = {}                               # pierwsze uruchomienie - pliku jeszcze nie ma

person_name = input('Name of the person you are voting for: ')
if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] = 1

with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(votes, file, indent=4)         # json.dump - zapisuje słownik do pliku JSON

print('Current results:', votes)
