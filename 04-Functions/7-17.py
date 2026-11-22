# Czy tekst jest palindromem
def f(palindrome):
    # [::-1] odwraca tekst
    return palindrome == palindrome[::-1]


def main():
    for text in ["radar", "12-11-21", "book"]:
        print(f'f("{text}") returns {f(text)}')


if __name__ == "__main__":
    main()
