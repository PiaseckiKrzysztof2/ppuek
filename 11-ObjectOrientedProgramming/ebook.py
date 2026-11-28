# Zadanie 11-4.4 - Moduł ebook (klasa EBook)
# Co robi: MODUŁ z klasą EBook: e-book ma tytuł, autora, liczbę stron i aktualną stronę.
#          Można go otworzyć i zamknąć; przewracać strony da się tylko, gdy jest otwarty.


class EBook:
    def __init__(self, title, author, pages):    # dane podane przy tworzeniu obiektu
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def next_page(self):
        if not self.is_open:
            print('The book is closed. Open it first!')
        elif self.current_page < self.pages:
            self.current_page += 1

    def previous_page(self):
        if not self.is_open:
            print('The book is closed. Open it first!')
        elif self.current_page > 1:
            self.current_page -= 1

    def show_status(self):
        state = 'open' if self.is_open else 'closed'
        print(f'"{self.title}" by {self.author}, {self.pages} pages, '
              f'current page {self.current_page}, book is {state}')
