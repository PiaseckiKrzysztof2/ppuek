# Zadanie 11-4.6 - Konto bankowe
# Co robi: klasa BankAccount ma numer konta i saldo (na start 0 zł). Można wpłacać,
#          wypłacać (tylko jeśli starczy pieniędzy) i wyświetlać numer oraz saldo.
#          Program: wpłata 25,30; wypłata 31,70 (za mało środków); wypłata 14 -> saldo 11,30.


class BankAccount:
    def __init__(self, number):              # STANY: numer i saldo
        self.number = number
        self.balance = 0.0

    def deposit(self, amount):               # ZACHOWANIA: wpłata, wypłata, wyświetlenie
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds on the account")
        else:
            self.balance -= amount

    def display(self):
        balance_text = f'{self.balance:.2f}'.replace('.', ',')   # 25.38 -> 25,38 (polski przecinek)
        print(f'Bank Account No: {self.number}')
        print(f'Balance: PLN {balance_text}')
        print()


account = BankAccount('12 3456 5555 9090 1111 0000 7722')
account.display()
account.deposit(25.30)
account.display()
account.withdraw(31.70)                      # więcej niż na koncie -> komunikat
account.display()
account.withdraw(14)
account.display()
