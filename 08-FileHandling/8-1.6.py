# Zadanie 8-1.6 - Kraje posortowane alfabetycznie
# Co robi: wczytuje cały plik countries.txt naraz, dzieli go na linijki
#          i wypisuje kraje w kolejności alfabetycznej.


def read_from_file(name):
    with open(name, 'r') as file:
        content = file.read()                # read() - cały plik jako JEDEN napis
    return content


file_content = read_from_file('countries.txt')

file_lines = file_content.splitlines()       # splitlines - dzieli napis na listę linijek

for line in sorted(file_lines):              # sorted - posortowana kopia listy
    print(line)
