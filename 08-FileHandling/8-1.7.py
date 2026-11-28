# Zadanie 8-1.7 - Suma zaparkowanych samochodów
# Co robi: w pliku car_park.txt jest liczba aut z 5 dni (jedna liczba w linijce).
#          Program sumuje te liczby i wypisuje wynik (85).


def read_from_file(name):
    with open(name) as file:
        content = file.read()
    return content


file_content = read_from_file('car_park.txt')
file_lines = file_content.splitlines()

total = 0                                    # schemat SUMY
for line in file_lines:
    total += int(line)                       # z pliku zawsze czytamy NAPIS -> int zamienia na liczbę

print('Total cars parked:', total)
