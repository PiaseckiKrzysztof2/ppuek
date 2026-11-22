# Czy liczba jest w przedziale <2, 15>
import ranges


def main():
    x, y = 2, 15
    number = int(input('A number: '))
    answer = 'yes' if ranges.in_range(number, x, y) else 'no'  # yes albo no
    print(f'Number {number} in the range <{x},{y}>: {answer}')


if __name__ == "__main__":
    main()
