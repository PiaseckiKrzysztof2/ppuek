# Zadanie 7-3.25 - Program używający modułu MyText
# Co robi: dla zdania "An apple a day keeps the doctor away" wypisuje liczbę słów (8),
#          słowa od najdłuższego i słowa alfabetycznie - funkcjami z modułu MyText.

import MyText

text = 'An apple a day keeps the doctor away'

print('Text:', text)
print('Number of words:', MyText.word_count(text))
print('Words from the longest:', ','.join(MyText.words_by_length(text)))      # join - słowa po przecinku
print('Words ordered alphabetically:', ','.join(MyText.words_alphabetically(text)))
