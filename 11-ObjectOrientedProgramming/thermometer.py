# Zadanie 11-4.5 - Moduł thermometer (klasa Thermometer)
# Co robi: MODUŁ z klasą termometru lekarskiego. Gdy jest włączony, mierzy temperaturę
#          (losowo od 34.0 do 42.0, dokładność 0.1) i ją wyświetla. Od 37.0 dopisuje (fever),
#          od 41.0 dodatkowo CRITICAL TEMPERATURE!!

import random


class Thermometer:
    def __init__(self):
        self.is_on = False
        self.temperature = None              # None - jeszcze nic nie zmierzono

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def measure(self):
        if self.is_on:
            self.temperature = round(random.uniform(34.0, 42.0), 1)   # uniform - losowa liczba z kropką
        else:
            print('Thermometer is off.')

    def display(self):
        if self.temperature is None:
            print('No measurement.')
            return
        message = f'Temperature: {self.temperature}C'
        if self.temperature >= 37.0:
            message += ' (fever)'
        print(message)
        if self.temperature >= 41.0:
            print('CRITICAL TEMPERATURE!!')
