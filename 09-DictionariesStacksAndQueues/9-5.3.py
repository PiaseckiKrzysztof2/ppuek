# Zadanie 9-5.3 - Słownik angielsko-polski
# Co robi: użytkownik wpisuje angielskie słowo, a program podaje polskie tłumaczenie
#          ze słownika albo informuje, że tłumaczenia nie ma.

translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

word = input('English word: ').lower()       # lower - małe litery, żeby 'Mouse' też działało

if word in translations:                     # czy jest taki klucz
    print('Polish:', translations[word])
else:
    print('Translation unavailable.')
