# Zadanie 7-2.5 - Miejsca w kinie
# Co robi: sala 5x5, 'A' = wolne (Available), 'B' = zajęte (Booked). Funkcje liczą
#          wszystkie miejsca, wolne i zajęte oraz podają status konkretnego miejsca (rząd, miejsce).

cinema_seats = [
    ['A', 'A', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A']
]


def seats_total(seats):
    total = 0
    for row in seats:
        total += len(row)
    return total


def count_seats(seats, status):
    counter = 0                               # LICZNIK w tablicy 2D - pętla w pętli
    for row in seats:
        for seat in row:
            if seat == status:
                counter += 1
    return counter


def seats_available(seats):
    return count_seats(seats, 'A')


def seats_booked(seats):
    return count_seats(seats, 'B')


def seat_status(seats, row, place):
    if seats[row - 1][place - 1] == 'A':      # - 1, bo rzędy liczymy od 1, a indeksy od 0
        return 'available'
    return 'booked'


print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))
