# Kalkulator - wynik działania dla podanego operatora
def f(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '%':
        return number1 % number2  # reszta z dzielenia
    elif operator == '**':
        return number1 ** number2  # potęga
    else:
        return None  # nieznany operator


def main():
    for op in ['+', '%', '**', '*', '-']:
        print(f'f(2,3, "{op}") returns {f(2, 3, op)}')


if __name__ == "__main__":
    main()
