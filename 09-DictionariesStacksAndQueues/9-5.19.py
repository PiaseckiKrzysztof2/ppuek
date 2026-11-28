# Zadanie 9-5.19 - Podsumowanie rezerwacji hotelowych
# Co robi: wczytuje rezerwacje z reservations.json i wypisuje: liczbę pokoi, liczbę
#          rezerwacji opłaconych i nieopłaconych oraz wartość jednych i drugich.
#          Wartość rezerwacji = liczba nocy x cena za noc.

import json


def load_reservations(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['reservations']              # w pliku jest słownik z kluczem "reservations" -> lista


def reservation_value(reservation):
    return reservation['nights'] * reservation['price_per_night']


def count_paid(reservations, paid):
    counter = 0
    for r in reservations:
        if r['paid'] == paid:                # paid=True - opłacone, paid=False - nieopłacone
            counter += 1
    return counter


def total_value(reservations, paid):
    total = 0
    for r in reservations:
        if r['paid'] == paid:
            total += reservation_value(r)
    return total


def main():
    reservations = load_reservations('reservations.json')
    print('Number of rooms:', len(reservations))
    print('Number of paid reservations:', count_paid(reservations, True))
    print('Number of unpaid reservations:', count_paid(reservations, False))
    print(f'Total value of paid reservations: {total_value(reservations, True):.2f}')
    print(f'Total value of unpaid reservations: {total_value(reservations, False):.2f}')


if __name__ == "__main__":
    main()
