# Zadanie 7-3.31 - Tworzenie tablicy 2D z zerami
# Co robi: funkcja create_2d_arr(x, y) tworzy tablicę x wierszy na y kolumn wypełnioną zerami.
#          Program tworzy tablicę 3x5 i ją wypisuje.


def create_2d_arr(x, y):
    return [[0 for col in range(y)] for row in range(x)]    # każdy wiersz to OSOBNA lista


array = create_2d_arr(3, 5)
for row in array:
    print(row)
