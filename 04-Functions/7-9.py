# Suma cyfr parzystych lub nieparzystych
def f(number, even):
    total = 0
    for char in str(abs(number)):
        digit = int(char)
        # parzysta, gdy reszta z dzielenia przez 2 to 0
        is_even = digit % 2 == 0
        if is_even == even:
            total += digit
    return total


def main():
    tests = [(3124, True), (3124, False), (20576, False), (20576, True), (13115, True)]
    for number, even in tests:
        print(f'f({number},{even}) returns {f(number, even)}')


if __name__ == "__main__":
    main()
