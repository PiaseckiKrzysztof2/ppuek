# Zadanie 11-2.2 - Klasa Song z __str__
# Co robi: klasa Song opisuje utwór (wykonawca, tytuł, album, rok). Metoda __str__
#          zwraca te dane w 4 linijkach. Program tworzy dwa utwory i je wypisuje.


class Song:
    def __init__(self, artist, title, album, year):     # konstruktor ustawia dane przy tworzeniu
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        return (f"Performer: {self.artist}\n"            # \n - nowa linia w napisie
                f"Title:     {self.title}\n"
                f"Album:     {self.album}\n"
                f"Year:      {self.year}\n")


song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Song("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)

print(song1)                                 # print wywołuje __str__
print(song2)
