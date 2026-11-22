# Zadanie 7-3.15 - Czy liczba jest w tablicy
# Co robi: funkcja occurs zwraca True, jeśli liczba jest w liście. Program wczytuje liczbę
#          z klawiatury i wypisuje, czy występuje w [15, 38, 7, 23, 14].


def occurs(number, array):
    for element in array:
        if element == number:
            return True                       # znalazłem -> od razu kończę z True
    return False                              # przeszedłem całą listę i nie znalazłem


array = [15, 38, 7, 23, 14]
number = int(input('Number: '))
print('Array:', ' '.join(str(x) for x in array))
if occurs(number, array):
    print(f'Result: number {number} appears in the array')
else:
    print(f'Result: number {number} does not appear in the array')
