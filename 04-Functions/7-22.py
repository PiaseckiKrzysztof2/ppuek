# Akronim - pierwsze litery słów
def f(name):
    result = ''
    # split dzieli tekst na słowa
    for word in name.split():
        result += word[0]  # pierwsza litera słowa
    return result


def main():
    for text in ["Internet of Things", "For Your Information", "Python"]:
        print(f'f("{text}") returns "{f(text)}"')


if __name__ == "__main__":
    main()
