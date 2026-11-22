# Najmniejsza liczba monet 1, 2, 5 zł do zapłaty
def f(amount_to_pay):
    coins = 0
    # najpierw biorę jak najwięcej największych monet
    for coin in [5, 2, 1]:
        coins += amount_to_pay // coin  # ile monet tego rodzaju
        amount_to_pay = amount_to_pay % coin  # ile zostało do zapłaty
    return coins


def main():
    for amount in [23, 8, 2, 0]:
        print(f'f({amount}) returns {f(amount)}')


if __name__ == "__main__":
    main()
