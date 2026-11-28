# Zadanie 8-4.3 (część b) - Obsługa błędu try-except (read_file_try_except.py)
# Co robi: próbuje otworzyć nieistniejący plik xyz.txt, ale w bloku try-except.
#          Zamiast się wywalić, program wypisuje komunikat i działa dalej.

file_name = 'xyz.txt'

try:                                         # try - spróbuj wykonać kod, który może dać błąd
    with open(file_name) as file:
        content = file.read()
except FileNotFoundError:                    # except - co zrobić, gdy pojawi się TEN błąd
    print(f"Hey! The file {file_name} does not exist.")

print('The program is still running.')
