# Zadanie 7-3.33 - Min i max w tablicy 2D z pozycją
# Co robi: znajduje najmniejszą i największą liczbę w tablicy 2D i podaje,
#          w którym wierszu i kolumnie leżą (-38: wiersz 1, kol. 1; 40: wiersz 2, kol. 2).

array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

min_value, min_row, min_col = array[0][0], 0, 0     # pamiętamy wartość i jej pozycję
max_value, max_row, max_col = array[0][0], 0, 0

for r in range(len(array)):
    for c in range(len(array[r])):
        if array[r][c] < min_value:                 # schemat MIN
            min_value, min_row, min_col = array[r][c], r, c
        if array[r][c] > max_value:                 # schemat MAX
            max_value, max_row, max_col = array[r][c], r, c

print(f'Smallest value: {min_value} (row {min_row + 1}, column {min_col + 1})')   # + 1 - numeracja od 1
print(f'Largest value: {max_value} (row {max_row + 1}, column {max_col + 1})')
