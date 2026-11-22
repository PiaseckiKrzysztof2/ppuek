# Sprawdza, czy hasło jest poprawne
def f(password):
    if len(password) < 6:
        return False
    for char in password:
        if password.count(char) > 1:  # znak się powtarza
            return False
    return True


def main():
    for pwd in ["ax15", "book123", "A2water3", "qwerty", ""]:
        print(f'f("{pwd}") returns {f(pwd)}')


if __name__ == "__main__":
    main()
