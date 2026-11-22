# Zadanie 7-1.15 - Sortowanie bąbelkowe (bubble sort)
# Co robi: funkcja bubble_sort sortuje listę rosnąco: porównuje SĄSIEDNIE elementy
#          i zamienia je miejscami, gdy lewy jest większy od prawego. Po każdym przejściu
#          największy element "wypływa" na koniec. Program sortuje spalanie aut i transakcje.


def bubble_sort(arr):
    arr = arr.copy()                          # kopia, żeby nie zmieniać oryginalnej listy
    n = len(arr)
    for i in range(n - 1):                    # ile przejść przez listę
        for j in range(n - i - 1):            # porównywanie sąsiadów w jednym przejściu
            if arr[j] > arr[j + 1]:           # lewy większy od prawego -> zła kolejność
                arr[j], arr[j + 1] = arr[j + 1], arr[j]   # zamiana miejscami (swap)
    return arr


car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
print(car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)
print(sorted_car_fuel_consumption)

bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
print(bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions)
print(sorted_bank_transactions)
