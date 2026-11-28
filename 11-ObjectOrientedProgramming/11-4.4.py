# Zadanie 11-4.4 - Używanie e-booka
# Co robi: tworzy e-book (klasa z modułu ebook.py), otwiera go, czyta kilka stron,
#          pokazuje stan, zamyka i próbuje czytać dalej - wtedy dostaje komunikat, że książka jest zamknięta.

from ebook import EBook                      # z pliku ebook.py weź klasę EBook


def main():
    book = EBook('The Hobbit', 'J.R.R. Tolkien', 310)    # 1. tworzenie z danymi (konstruktor)

    book.open()                              # 2.
    book.show_status()                       # 3.
    for i in range(4):                       # 4. czytamy 4 strony
        book.next_page()
    book.show_status()                       # 5.
    book.close()                             # 6.
    book.next_page()                         # 7. książka zamknięta -> komunikat


if __name__ == "__main__":
    main()
