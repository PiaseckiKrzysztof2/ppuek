# Zadanie 9-2.5 - Połączenie list kontaktów
# Co robi: łączy dwa zbiory e-maili w jeden; adres, który był w obu, pojawia się tylko raz.

contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}
contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}

merged_contacts = contacts_A | contacts_B   # | - suma: wszystko z obu zbiorów, bez powtórzeń
print("Merged contacts:", merged_contacts)
