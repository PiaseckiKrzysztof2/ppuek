# Program testujący funkcje wbudowane
# funkcji wbudowanych nie trzeba importować

max_number = max(7, 5, 6, 3, 8, 2)  # największa liczba
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4, 7, 2, 3, 9, 8)  # najmniejsza liczba
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")  # długość tekstu
print('The number of characters in "computer science" is', str_length)

letter = input('Enter a letter: ')  # input zawsze zwraca tekst
print('You entered the letter:', letter)

number = int("20303")  # zamiana tekstu na liczbę
print('Number representing the string "20303" is', number)

binary = bin(304)  # zapis binarny
print('Binary string of 304 is', binary)

hexadecimal = hex(304)  # zapis szesnastkowy
print('Hexadecimal string of 304 is', hexadecimal)

euro_code = ord('€')  # kod znaku w Unicode
print('Unicode code of the € sign is', euro_code)

absolute = abs(-17)  # wartość bezwzględna
print('Absolute value of -17 is', absolute)
