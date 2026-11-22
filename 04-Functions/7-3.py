# Nazwa miesiąca - korzysta z modułu months
from months import month  # importuję tylko funkcję month


def main():
    print('The name of month 7 is', month(7))

    number = int(input('Enter month number: '))
    print(f'The name of month {number} is {month(number)}')


if __name__ == "__main__":
    main()
