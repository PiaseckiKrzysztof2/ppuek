# Zadanie 9-2.6 - Uprawnienia użytkownika
# Co robi: sprawdza, czy użytkownik ma WSZYSTKIE wymagane uprawnienia.
#          Wynik to False, bo brakuje mu uprawnienia "execute".

required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

has_permissions = required_permissions.issubset(user_permissions)   # issubset - czy wszystkie wymagane są u użytkownika
print(has_permissions)
