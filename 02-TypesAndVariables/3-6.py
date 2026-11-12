import math                                             # Import modułu matematycznego
h = float(input('Enter height in meters: '))
d = 3.57 * math.sqrt(h)
print('Distance to the horizon:', round(d, 2), 'km')    # Wyświetla wynik zaokrąglony do 2 miejsc po przecinku