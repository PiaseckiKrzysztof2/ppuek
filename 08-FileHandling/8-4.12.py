# Zadanie 8-4.12 - Książki według gatunku do osobnych plików
# Co robi: czyta listę książek z books.csv i zapisuje książki z gatunków Fantasy,
#          Historical, Romance i Classic do osobnych plików (np. books_fantasy.txt).
#          Program jest podzielony na funkcje.

import csv

genre_files = {                              # słownik: gatunek -> nazwa pliku
    'Fantasy': 'books_fantasy.txt',
    'Historical': 'books_historical.txt',
    'Romance': 'books_romance.txt',
    'Classic': 'books_classic.txt',
}


def read_books(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return list(csv.DictReader(file))    # lista słowników, jeden na książkę


def books_by_genre(books, genre):
    result = []
    for book in books:
        if book['Genre'] == genre:
            result.append(book)
    return result


def save_books(file_name, books):
    with open(file_name, 'w', encoding='utf-8') as file:
        for book in books:
            file.write(f"{book['Title']},{book['Author']},{book['Genre']},{book['Year']}\n")


def main():
    books = read_books('books.csv')
    for genre, file_name in genre_files.items():
        selected = books_by_genre(books, genre)
        save_books(file_name, selected)
        print(f'{genre} --> {file_name} ({len(selected)} books)')


if __name__ == "__main__":
    main()
