# Zadanie 8-4.3 (część a) - Otwarcie pliku, którego nie ma (read_file.py)
# Co robi: próbuje otworzyć nieistniejący plik xyz.txt. Program się WYWALA
#          z błędem FileNotFoundError - tak ma być, to przykład z repo.
#          Porównaj z 8-4.3b.py, gdzie błąd jest obsłużony przez try-except.

file_name = 'xyz.txt'                        # takiego pliku nie ma na dysku

with open(file_name) as file:                # tu program się zatrzyma z błędem
    content = file.read()
