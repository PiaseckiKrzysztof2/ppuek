# Zadanie 7-1.10 - Statystyki testu
# Co robi: lista zawiera odpowiedzi ucznia (True - dobrze, False - źle). Program wypisuje
#          liczbę pytań, liczbę dobrych i złych odpowiedzi oraz procent dobrych.

test_results = [
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False
]

question_number = len(test_results)

correct_answers = 0                           # schemat LICZNIKA
for answer in test_results:
    if answer:                                # answer to już True/False
        correct_answers = correct_answers + 1

incorrect_answers = question_number - correct_answers

percentage = correct_answers / question_number * 100

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print(f'Percentage of correct answers: {percentage:.1f}%')   # :.1f - 1 miejsce po przecinku
