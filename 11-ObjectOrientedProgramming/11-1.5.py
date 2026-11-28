# Zadanie 11-1.5 - Książka z ceną (book.py)
# Co robi: klasa Book opisuje książkę (tytuł, autor, strony, czy otwarta, aktualna strona).
#          Dodana jest cena, podawana przy tworzeniu obiektu (48), i wypisywana z resztą danych.


class Book():
    def __init__(self, title, author, pages, price):    # price - nowy parametr konstruktora
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.current_page = 1
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def change_page(self, page):
        self.current_page = page

    def display_info(self):
        print(f"My favourite book is {self.title}.")
        print(f"Written by {self.author}.")
        print(f"This book has {self.pages} pages.")
        print(f"It costs {self.price} PLN.")
        if self.is_open:
            print(f"I am just reading the book, page {self.current_page}.")
        else:
            print("I am going to read the book later.")


def main():
    favourite_book = Book(
        "Harry Potter and the Philosopher's Stone",
        "J. K. Rowling", 223, 48)            # 48 - cena

    favourite_book.open()
    favourite_book.change_page(15)
    favourite_book.display_info()
    favourite_book.close()


if __name__ == "__main__":
    main()
