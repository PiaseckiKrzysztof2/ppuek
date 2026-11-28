# Zadanie 11-4.7 - Klasa Statistics
# Co robi: klasa Statistics przechowuje liczby w liście. Liczby wczytuje się z klawiatury
#          (pusta linijka kończy). Potem liczy i wypisuje: wszystkie liczby, min, max,
#          średnią i medianę. Dla 12, 37, 6, 9, 17: min 6, max 37, średnia 16.2, mediana 12.


class Statistics:
    def __init__(self):
        self.numbers = []

    def add_number(self):
        text = input('Enter a number (empty line ends): ')
        if text == '':
            return False                     # sygnał, że to koniec wpisywania
        self.numbers.append(float(text))
        return True

    def show_numbers(self):
        print('Numbers:', ' '.join(f'{n:g}' for n in self.numbers))   # :g - bez zbędnego .0

    def maximum(self):
        return max(self.numbers)

    def minimum(self):
        return min(self.numbers)

    def mean(self):
        return sum(self.numbers) / len(self.numbers)

    def median(self):
        ordered = sorted(self.numbers)       # mediana = środek POSORTOWANEJ listy
        n = len(ordered)
        middle = n // 2
        if n % 2 == 1:
            return ordered[middle]
        return (ordered[middle - 1] + ordered[middle]) / 2

    def print_statistics(self):
        print(f'Minimum: {self.minimum():g}')
        print(f'Maximum: {self.maximum():g}')
        print(f'Mean:    {self.mean():g}')
        print(f'Median:  {self.median():g}')


stats = Statistics()
while stats.add_number():                    # wczytuj, dopóki add_number zwraca True
    pass                                     # pass - "nic nie rób", pętla sama wszystko robi

if stats.numbers:
    stats.show_numbers()
    stats.print_statistics()
