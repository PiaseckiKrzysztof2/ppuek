# Suma powtarzających się cyfr
def f(number):
    digits = str(number)
    total = 0
    for char in digits:
        # count liczy, ile razy cyfra występuje
        if digits.count(char) > 1:
            total += int(char)
    return total


def main():
    for number in [1027, 230335, 513553007]:
        print(f'f({number}) returns {f(number)}')


if __name__ == "__main__":
    main()
