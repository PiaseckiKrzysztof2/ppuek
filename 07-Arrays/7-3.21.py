# Zadanie 7-3.21 - Ile elementów większych od podanej wartości
# Co robi: wczytuje liczbę z klawiatury i liczy, ile liczb z listy jest od niej większych.

numbers = [3.5, 7.2, -1.4, 10.0, 5.5, 2.25, 8.75]

print('Array:', numbers)
limit = float(input('Enter value: '))         # float, bo liczby w liście mają kropkę

counter = 0                                   # schemat LICZNIKA
for x in numbers:
    if x > limit:
        counter += 1

print(f'Number of elements greater than {limit}: {counter}')
