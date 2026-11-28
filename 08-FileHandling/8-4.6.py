# Zadanie 8-4.6 - Linie, znaki i słowa w pliku
# Co robi: użytkownik wpisuje nazwę pliku tekstowego, a program liczy w nim linijki,
#          znaki i słowa. Jeśli pliku nie ma, try-except wypisuje komunikat zamiast błędu.
#          Do testów możesz użyć np. pets.txt, books.csv albo healthy_lifestyle.txt.

file_name = input('File name: ')

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    lines = len(content.splitlines())        # liczba linijek
    characters = len(content)                # liczba znaków
    words = len(content.split())             # liczba słów

    print('Number of lines:', lines)
    print('Number of characters:', characters)
    print('Number of words:', words)
except FileNotFoundError:
    print(f'File {file_name} does not exist.')
