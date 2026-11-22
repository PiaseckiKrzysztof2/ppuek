# Czy napis jest liczbą binarną
def f(binary_number):
    if binary_number == '':  # pusty tekst to nie liczba
        return False
    for char in binary_number:
        if char not in '01':  # znak inny niż 0 i 1
            return False
    return True


def main():
    print('f("101101") returns', f("101101"))
    print('f("1311a10100") returns', f("1311a10100"))


if __name__ == "__main__":
    main()
