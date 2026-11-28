# Zadanie 11-4.8 - Moduł contact (klasa Contact)
# Co robi: MODUŁ z klasą Contact opisującą jeden kontakt: imię i nazwisko, e-mail, telefon.


class Contact:
    def __init__(self, name, email, telephone):
        self.name = name
        self.email = email
        self.telephone = telephone

    def __str__(self):
        return f'{self.name:<15}{self.email:<20}{self.telephone}'   # :<15 - kolumny równej szerokości
