# Zadanie 11-3.6 - Głośność 0-10
# Co robi: sprawdza regulację głośności: podgłaśnia 12 razy (zatrzyma się na 10),
#          potem ścisza 12 razy (zatrzyma się na 0) i za każdym razem pokazuje stan.

import tv


def main():
    my_tv = tv.TV()
    my_tv.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN'])
    my_tv.turn_on()
    my_tv.show_status()

    for i in range(12):
        my_tv.volume_up()                    # powyżej 10 już nie rośnie
    my_tv.show_status()

    my_tv.volume_down()
    my_tv.volume_down()
    my_tv.show_status()

    for i in range(12):
        my_tv.volume_down()                  # poniżej 0 już nie spada
    my_tv.show_status()


if __name__ == "__main__":
    main()
