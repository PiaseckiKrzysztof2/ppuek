# Zadanie 11-4.8 - Kontakty w smartfonie (w treści zadania: smartphone.py)
# Co robi: program główny. Tworzy listę kontaktów (klasa z contact_list.py), dodaje
#          4 osoby i wyświetla listę. Program składa się z 3 plików: ten, contact.py, contact_list.py.

from contact_list import Contact_List


def main():
    phone_contacts = Contact_List()

    phone_contacts.add_contact('John Brown', 'brown@onet.pl', '555234000')
    phone_contacts.add_contact('Anna May', 'am@o2.pl', '232000199')
    phone_contacts.add_contact('George Small', 'smallg@google.pl', '222999100')
    phone_contacts.add_contact('Paola Big', 'bigpaola@poczta.pl', '100200300')

    phone_contacts.display()


if __name__ == "__main__":
    main()
