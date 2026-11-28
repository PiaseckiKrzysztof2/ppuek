# Zadanie 9-2.4 - Wykrywanie spamu
# Co robi: znajduje adresy, które są jednocześnie w odebranej poczcie i na liście spamu
#          (część wspólna zbiorów).

emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}
spam_list = {"spam1@example.com", "spam2@example.com"}

spam_emails = emails_received & spam_list   # & - część wspólna: elementy w OBU zbiorach
print("Spam emails:", spam_emails)
