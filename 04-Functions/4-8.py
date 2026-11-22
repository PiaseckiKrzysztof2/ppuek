# Godzina jako napis w formacie 24h lub 12h
def time_string(hours, minutes, time_format):
    # 02d dopisuje zero z przodu, np. 08
    if time_format == '24':
        return f'{hours:02d}:{minutes:02d}'

    # format 12h: am przed południem, pm po południu
    if hours < 12:
        suffix = 'am'
    else:
        suffix = 'pm'

    hours_12 = hours % 12  # reszta z dzielenia przez 12
    if hours_12 == 0:
        hours_12 = 12  # 0 i 12 to godzina 12

    return f'{hours_12}:{minutes:02d}{suffix}'


# testy z zadania
tests = [
    (15, 38, '24', '15:38'),
    (8, 3, '24', '08:03'),
    (0, 5, '24', '00:05'),
    (11, 15, '12', '11:15am'),
    (0, 7, '12', '12:07am'),
    (7, 30, '12', '7:30am'),
    (12, 46, '12', '12:46pm'),
    (13, 10, '12', '1:10pm'),
    (19, 2, '12', '7:02pm'),
]

for h, m, fmt, expected in tests:
    result = time_string(h, m, fmt)
    status = 'OK' if result == expected else 'ERROR'  # OK jeśli wynik się zgadza
    print(f"time_string({h}, {m}, '{fmt}') returns '{result}' -> {status}")
