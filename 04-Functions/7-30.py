# Suma liczb od 1 do n rekurencyjnie
def sum_natural(n):
    if n == 1:  # warunek końca
        return 1
    return n + sum_natural(n - 1)  # sum(n) = n + sum(n-1)


def main():
    print('Sum of natural numbers in the range <1,10>:', sum_natural(10))


if __name__ == "__main__":
    main()
