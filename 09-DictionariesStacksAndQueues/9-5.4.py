# Zadanie 9-5.4 - Suma godzin w semestrze
# Co robi: sumuje godziny wszystkich przedmiotów z semestru zimowego (60 + 30 + 15 = 105).

winter_semester = {
    "math": 60,
    "programming": 30,
    "history": 15
}

total = 0
for hours in winter_semester.values():       # values - same wartości (godziny)
    total += hours

print(f'The total number of hours in the winter semester is {total}')
