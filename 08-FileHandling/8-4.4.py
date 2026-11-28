# Zadanie 8-4.4 - Wyświetlanie pliku po 5 linijek
# Co robi: wypisuje plik it_company.csv po 5 linijek. Po każdej piątce pisze
#          'Press Enter key...' i czeka, aż użytkownik naciśnie Enter.

lines_per_page = 5

with open('it_company.csv', 'r') as file:
    counter = 0
    for line in file:
        print(line, end="")
        counter += 1
        if counter % lines_per_page == 0:    # co 5 linijek (5, 10, 15...) reszta z dzielenia = 0
            input('Press Enter key...')      # input czeka na Enter
