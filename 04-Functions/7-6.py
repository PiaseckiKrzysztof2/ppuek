# Maskuje numer karty kredytowej
from cards import hide


def main():
    card = "5290312400019022"
    print(f'f("{card}") returns "{hide(card)}"')


if __name__ == "__main__":
    main()
