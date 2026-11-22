# Silnia liczona rekurencyjnie
# rekurencja - funkcja wywołuje samą siebie
# musi mieć warunek końca, inaczej wywołuje się w nieskończoność


def factorial(n):
    # 0! = 1, 1! = 1
    if n == 0 or n == 1:
        return 1

    # n! = n * (n-1)!
    if n > 1:
        return n * factorial(n - 1)


def main():
    print('5! =', factorial(5))


if __name__ == "__main__":
    main()
