# Potęga x^n rekurencyjnie
def power(x, n):
    if n == 0:  # x^0 = 1
        return 1
    return x * power(x, n - 1)  # x^n = x * x^(n-1)


def main():
    print('5^3 =', power(5, 3))


if __name__ == "__main__":
    main()
