# Zadanie 7-2.2 - Plansza kółko i krzyżyk
# Co robi: plansza 3x3 jest zapisana jako lista list (tablica 2D).
#          Program wypisuje ją na ekranie wiersz po wierszu.

tic_tac_toe_board = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]

for row in tic_tac_toe_board:     # pętla po wierszach
    for cell in row:              # pętla w pętli - po komórkach wiersza
        print(cell, end=" ")      # komórki w jednej linii
    print()                       # koniec wiersza -> nowa linia
