# Zadanie 8-2.1 - Zapis danych filmu do pliku (movie.py)
# Co robi: zapisuje do pliku movie_details.txt tytuł filmu, reżysera i głównego aktora,
#          każdą informację w osobnej linijce. Po uruchomieniu otwórz ten plik i sprawdź.

movie_title = "Inception"
director = "Christopher Nolan"
lead_actor = "Leonardo DiCaprio"

file_name = 'movie_details.txt'

with open(file_name, 'w') as file:           # 'w' - tryb zapisu (write): tworzy plik albo go NADPISUJE
    file.write(f"Movie Title: {movie_title}\n")      # \n - przejście do nowej linii
    file.write(f"Director: {director}\n")
    file.write(f"Lead Actor: {lead_actor}\n")

print(f"Movie details have been written to {file_name}.")
