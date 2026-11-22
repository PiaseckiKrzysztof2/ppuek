# n-ty wyraz ciągu Fibonacciego
def f(n):
    a, b = 0, 1  # dwa pierwsze wyrazy
    for i in range(n - 1):
        # następny wyraz to suma dwóch poprzednich
        a, b = b, a + b
    return a


def main():
    print('f(5) returns', f(5))
    print('f(9) returns', f(9))


if __name__ == "__main__":
    main()
