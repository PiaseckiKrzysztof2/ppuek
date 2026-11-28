# Zadanie 11-3.5 - Nazwa kanału w statusie
# Co robi: ustawia 7 kanałów i kilka razy zmienia kanał. show_status wypisuje też nazwę
#          kanału, np. "channel 4 (TVN)"; dla numeru spoza listy (np. 9) nazwy nie ma.

import tv


def main():
    my_tv = tv.TV()
    my_tv.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery', 'TVP Sport'])
    my_tv.turn_on()

    for channel in [1, 4, 7, 9, 2]:          # 9 - nie ma takiego kanału na liście
        my_tv.set_channel(channel)
        my_tv.show_status()


if __name__ == "__main__":
    main()
