# Zadanie 11-4.11 - Stadion (klasa C)
# Co robi: klasa C dostaje słownik sektor: liczba kibiców. m1(s, n) zmienia liczbę kibiców
#          w sektorze s albo dodaje nowy sektor. m2(s) sumuje kibiców z sektorów wymienionych
#          w napisie s (sektory, których nie ma, pomija). m2("GD") = 280, m2("KEJ") = 110.


class C:
    def __init__(self, sectors):
        self.sectors = sectors               # słownik, np. {"A": 120, "D": 150}

    def m1(self, s, n):
        self.sectors[s] = n                  # ten sam zapis zmienia albo dodaje klucz

    def m2(self, s):
        total = 0
        for sector in s:                     # pętla po literach napisu, np. "G", "D"
            if sector in self.sectors:       # nie ma takiego sektora -> pomijamy
                total += self.sectors[sector]
        return total


stadium = C({"A": 120, "D": 150, "G": 90, "K": 110})
stadium.m1("G", 130)
print('m2("GD") returns', stadium.m2("GD"))
print('m2("KEJ") returns', stadium.m2("KEJ"))
