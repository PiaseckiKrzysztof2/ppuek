# Suma cyfr liczby
def sum_digits(number):
    number = abs(number)  # abs, żeby działało też dla ujemnych
    total = 0
    # zamieniam liczbę na tekst, żeby przejść po cyfrach
    for digit in str(number):
        total += int(digit)  # cyfra z powrotem na int
    return total


any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')
