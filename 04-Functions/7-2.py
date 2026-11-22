# Przykład if __name__ == "__main__" i funkcji main()
# __name__ == "__main__" jest tylko wtedy, gdy uruchamiam ten plik,
# a nie gdy go importuję


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def main():
    # główny program w funkcji main
    x = 10
    y = 5
    print(f"Add: {add(x, y)}")
    print(f"Subtract: {subtract(x, y)}")


if __name__ == "__main__":
    main()
