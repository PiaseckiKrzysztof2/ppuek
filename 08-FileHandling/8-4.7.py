# Zadanie 8-4.7 - Liczba samogłosek
# Co robi: wczytuje tekst z klawiatury i wyrażeniem regularnym liczy w nim samogłoski
#          (a, e, i, o, u - małe i wielkie).

import re

text = input('Enter text: ')

vowels = re.findall(r'[aeiouAEIOU]', text)   # [...] - jeden z wymienionych znaków
print('Number of vowels:', len(vowels))      # findall zwraca listę, len - ile ich jest
