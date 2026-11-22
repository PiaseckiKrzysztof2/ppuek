# Zadanie 7-2.3 - Wydatki miesięczne
# Co robi: tabela 4x3: wiersz = tydzień, kolumny = Food, Transport, Utilities.
#          Program liczy sumę dla każdej kategorii (kolumny), każdego tygodnia (wiersza)
#          i całego miesiąca, a potem wypisuje raport.

monthly_expenses = [
    [200, 50, 100],
    [180, 60, 110],
    [220, 55, 105],
    [210, 65, 95]
]

rows = len(monthly_expenses)                  # liczba wierszy (tygodni)
cols = len(monthly_expenses[0])               # liczba kolumn (kategorii)

category_totals = [0] * cols                  # [0, 0, 0]
for c in range(cols):
    for r in range(rows):
        category_totals[c] += monthly_expenses[r][c]   # suma KOLUMNY: stałe c, zmienia się r

week_totals = []
for week in monthly_expenses:
    week_sum = 0
    for amount in week:                       # suma WIERSZA
        week_sum += amount
    week_totals.append(week_sum)              # append - dopisz na koniec listy

total = 0
for week_sum in week_totals:
    total += week_sum

print('MONTHLY EXPENSES')
print('----------------')
print('Food:', category_totals[0])
print('Transport:', category_totals[1])
print('Utilities:', category_totals[2])
print('Week 1:', week_totals[0])
print('Week 2:', week_totals[1])
print('Week 3:', week_totals[2])
print('Week 4:', week_totals[3])
print('---------------')
print('TOTAL:', total)
