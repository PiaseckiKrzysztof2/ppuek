# Zadanie 11-3.1 - Telewizor: włącz i wyłącz (tv_show.py)
# Co robi: tworzy telewizor z klasy TV (moduł tv.py), pokazuje jego stan,
#          włącza go, pokazuje stan, wyłącza i znowu pokazuje stan.

import tv                                    # moduł tv.py z klasą TV


def main():
    my_tv = tv.TV()                          # tworzenie obiektu klasy z modułu: moduł.Klasa()

    my_tv.show_status()
    my_tv.turn_on()
    my_tv.show_status()
    my_tv.turn_off()
    my_tv.show_status()


if __name__ == "__main__":
    main()
