# Zadanie 11-4.8 - Moduł contact_list (klasa Contact_List)
# Co robi: MODUŁ z klasą Contact_List, która trzyma kontakty (obiekty Contact) w liście
#          i pozwala dodać nowy kontakt oraz wyświetlić całą listę.

from contact import Contact


class Contact_List:
    def __init__(self):
        self.contacts = []                   # lista OBIEKTÓW klasy Contact

    def add_contact(self, name, email, telephone):
        self.contacts.append(Contact(name, email, telephone))    # tworzy obiekt Contact i dopisuje

    def display(self):
        print('CONTACT LIST')
        print('============')
        for contact in self.contacts:
            print(contact)                   # print wywołuje __str__ z klasy Contact
