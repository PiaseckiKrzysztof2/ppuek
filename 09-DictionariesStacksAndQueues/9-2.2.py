# Zadanie 9-2.2 - Usuwanie powtórzonych e-maili
# Co robi: zamienia listę e-maili na zbiór (set), przez co powtórzenia znikają.

emails = ["john@example.com", "jane@example.com", "john@example.com", "alex@example.com"]
unique_emails = set(emails)                  # set - zbiór: każdy element tylko RAZ, bez kolejności
print(unique_emails)
