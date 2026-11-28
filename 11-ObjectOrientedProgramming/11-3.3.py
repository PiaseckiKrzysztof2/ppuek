# Zadanie 11-3.3 - Zmiana kanału
# Co robi: tworzy telewizor, włącza go, zmienia kanał na 5 metodą set_channel
#          i po każdym kroku pokazuje stan.

import tv


def main():
    my_tv = tv.TV()

    my_tv.show_status()
    my_tv.turn_on()
    my_tv.show_status()
    my_tv.set_channel(5)                     # metoda z argumentem
    my_tv.show_status()
    my_tv.turn_off()
    my_tv.show_status()


if __name__ == "__main__":
    main()
