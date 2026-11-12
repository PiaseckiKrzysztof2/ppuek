# A program that checks whether the number entered
# from the keyboard is even.
number = int(input('Enter number: '))
even = number % 2 == 0                      # Sprawdza czy liczba jest parzysta
print(f'Number is even: {even}')