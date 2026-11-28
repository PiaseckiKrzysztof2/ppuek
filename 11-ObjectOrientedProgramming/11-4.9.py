# Zadanie 11-4.9 - Pracownik jako napis (klasa C)
# Co robi: klasa C przechowuje imię, nazwisko, wiek i staż pracownika. Jej __str__ zwraca:
#          nazwisko + pierwsza litera imienia + staż, wielkimi literami dla dorosłych (18+),
#          małymi dla niepełnoletnich. C("Anna","May",17,7) -> "maya7", C("George","Brown",21,4) -> "BROWNG4".


class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        text = f'{self.surname}{self.name[0]}{self.seniority}'   # name[0] - pierwsza litera imienia
        if self.age >= 18:
            return text.upper()              # upper - wielkie litery
        return text.lower()                  # lower - małe litery


print(f'C("Anna","May",17,7) returns "{C("Anna", "May", 17, 7)}"')
print(f'C("George","Brown",21,4) returns "{C("George", "Brown", 21, 4)}"')
