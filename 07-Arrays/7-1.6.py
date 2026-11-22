# Zadanie 7-1.6 - Dzień tygodnia z tablicy
# Co robi: funkcja weekday zwraca nazwę dnia z listy dla numeru 1-7.
#          Program wypisuje nazwy dni 1, 4 i 7 (Monday, Thursday, Sunday).


def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n - 1]        # n - 1, bo dzień 1 to indeks 0


for day in [1, 4, 7]:
    print(f'Day {day}: {weekday(day)}')
