# Zadanie 11-3.4 - Lista kanałów
# Co robi: pokazuje listę kanałów, gdy telewizor nie jest zaprogramowany (pusta),
#          potem ustawia 6 kanałów metodą set_channels i pokazuje listę jeszcze raz.

import tv


def main():
    my_tv = tv.TV()

    my_tv.show_status()
    my_tv.turn_on()
    my_tv.show_status()
    my_tv.show_channels()                    # jeszcze pusta lista
    my_tv.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery'])
    my_tv.show_channels()
    my_tv.show_status()
    my_tv.turn_off()


if __name__ == "__main__":
    main()
