# n gwiazdek rozdzielonych ukośnikiem
def f(n):
    result = ''
    for i in range(n):
        if i > 0:
            result += '/'  # ukośnik przed każdą gwiazdką oprócz pierwszej
        result += '*'
    return result


def main():
    print(f'f(4) returns "{f(4)}"')
    print(f'f(1) returns "{f(1)}"')


if __name__ == "__main__":
    main()
