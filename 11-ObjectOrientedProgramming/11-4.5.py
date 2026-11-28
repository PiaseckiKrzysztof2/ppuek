# Zadanie 11-4.5 - Używanie termometru
# Co robi: tworzy termometr (klasa z modułu thermometer.py), włącza go, mierzy temperaturę,
#          wyświetla wynik i wyłącza termometr.

from thermometer import Thermometer


def main():
    thermometer = Thermometer()              # 1.
    thermometer.turn_on()                    # 2.
    thermometer.measure()                    # 3.
    thermometer.display()                    # 4.
    thermometer.turn_off()                   # 5.


if __name__ == "__main__":
    main()
