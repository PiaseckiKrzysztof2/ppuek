# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
# TEST - BPKOPLPW, CHASUS33, DEUTDEFF. (PL, US, DE)
swift = input('Enter SWIFT code: ')   # Pobiera kod SWIFT
print(f'Bank Code: {swift[0:4]}')     # Wyświetla kod banku
print(f'Country Code: {swift[4:6]}')  # Wyświetla kod kraju