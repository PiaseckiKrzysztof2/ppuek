# Zadanie 7-3.16 - Krotka z jednym elementem
# Co robi: tworzy krotkę (tuple) z jednym słowem 'computation' i wypisuje jej typ.
#          Dla porównania pokazuje, że bez przecinka to nie jest krotka, tylko napis.

word_tuple = ('computation',)                 # PRZECINEK -> krotka (tuple)
not_a_tuple = ('computation')                 # bez przecinka -> zwykły napis (str)

print(word_tuple, type(word_tuple))           # type - jakiego typu jest wartość
print(not_a_tuple, type(not_a_tuple))
