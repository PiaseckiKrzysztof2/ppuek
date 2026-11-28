# Zadanie 11-1.3 - Kursy taksówką (taxi.py)
# Co robi: klasa TaxiRide liczy opłatę za kurs (odległość x stawka za km).
#          Dodana metoda print_receipt wypisuje paragon. Program tworzy dwa kursy i drukuje paragony.


class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km       # stawka w € za km
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km     # metoda zmienia atrybuty obiektu

    def print_receipt(self):                 # dodana metoda
        print('TAXI RECEIPT')
        print(f'Distance: {self.distance} km')
        print(f'Rate:     €{self.rate_per_km:.2f} per km')
        print(f'Fare:     €{self.fare:.2f}')
        print()


def main():
    ride1 = TaxiRide(2)                      # dwa RÓŻNE obiekty tej samej klasy
    ride2 = TaxiRide(2.5)

    ride1.calculate_fare(10)
    ride2.calculate_fare(7.5)

    ride1.print_receipt()
    ride2.print_receipt()


if __name__ == "__main__":
    main()
