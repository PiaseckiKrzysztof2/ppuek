# n-ta liczba pierwsza
def is_prime(number):
    # sprawdza, czy liczba jest pierwsza
    if number < 2:
        return False
    # wystarczy sprawdzać dzielniki do pierwiastka
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def f(n):
    found = 0  # ile pierwszych już znalazłem
    candidate = 1
    while found < n:
        candidate += 1
        if is_prime(candidate):
            found += 1
    return candidate


def main():
    print('f(1) returns', f(1))
    print('f(5) returns', f(5))


if __name__ == "__main__":
    main()
