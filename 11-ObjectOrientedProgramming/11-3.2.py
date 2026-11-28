# Zadanie 11-3.2 - Telewizor z numerem kanału
# Co robi: sprawdza, że show_status wypisuje numer kanału tylko wtedy,
#          gdy telewizor jest włączony ("TV is on, channel 1" / "TV is off").

import tv


def main():
    my_tv = tv.TV()

    my_tv.show_status()                      # wyłączony -> bez kanału
    my_tv.turn_on()
    my_tv.show_status()                      # włączony -> z kanałem
    my_tv.turn_off()
    my_tv.show_status()


if __name__ == "__main__":
    main()
