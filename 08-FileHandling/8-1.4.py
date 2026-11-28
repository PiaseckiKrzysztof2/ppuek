# Zadanie 8-1.4 - Odczyt pliku linijka po linijce (print_countries.py)
# Co robi: otwiera plik countries.txt i wypisuje go linijka po linijce.
#          To gotowy program z repo do przeanalizowania.

with open('countries.txt', 'r') as file:    # with - plik sam się zamknie; 'r' - tryb odczytu (read)
    for line in file:                        # pętla po pliku daje kolejne LINIJKI
        print(line, end="")                  # end="" - linijka ma już na końcu znak nowej linii \n
