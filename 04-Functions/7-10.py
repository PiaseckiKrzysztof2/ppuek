# Ile jest ujemnych liczb parzystych w przedziale <x, y>
def f(x, y):
    counter = 0
    # y + 1, bo range nie bierze ostatniej liczby
    for n in range(x, y + 1):
        if n < 0 and n % 2 == 0:
            counter += 1
    return counter


def main():
    print('f(-7,8) returns', f(-7, 8))
    print('f(-1,11) returns', f(-1, 11))


if __name__ == "__main__":
    main()
