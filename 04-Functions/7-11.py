# Czy choć jedna z trzech liczb jest ujemna
def f(n1, n2, n3):
    # wystarczy, że jedna jest ujemna
    return n1 < 0 or n2 < 0 or n3 < 0


def main():
    print('f(11,6,-4) returns', f(11, 6, -4))
    print('f(5,4,14) returns', f(5, 4, 14))


if __name__ == "__main__":
    main()
