# Zadanie 7-3.25 - Moduł MyText
# Co robi: MODUŁ z funkcjami do tekstu: liczba słów, słowa od najdłuższego
#          do najkrótszego, słowa alfabetycznie.


def word_count(text):
    return len(text.split())                  # split - lista słów, len - ile ich jest


def words_by_length(text):
    return sorted(text.split(), key=len, reverse=True)    # key=len - sortuj wg długości, malejąco


def words_alphabetically(text):
    return sorted(text.split(), key=str.lower)            # key=str.lower - alfabetycznie, bez znaczenia wielkość liter
