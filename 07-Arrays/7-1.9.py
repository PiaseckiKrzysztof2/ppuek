# Zadanie 7-1.9 - Rejestracje z Krakowa
# Co robi: z listy numerów rejestracyjnych wypisuje (ponumerowane) tylko te z Krakowa,
#          czyli zaczynające się od 'KR' albo 'KK'.

polish_license_plates = [
    'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
    'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
    'KK54985', 'LU4864U'
]

counter = 1
for car_number in polish_license_plates:
    if car_number.startswith(('KR', 'KK')):   # startswith - czy napis zaczyna się od KR lub KK
        print(counter, car_number)
        counter += 1
