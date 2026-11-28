# Zadanie 11-1.6 - Klasa Phone (smartfon)
# Co robi: klasa Phone ma 3 stany (atrybuty): markę, poziom baterii i czy jest włączony,
#          oraz zachowania (metody): włącz, wyłącz, zadzwoń, naładuj, pokaż informacje.
#          Program tworzy telefon, wywołuje metody i wypisuje jego stan.


class Phone():
    def __init__(self, brand, battery_level):
        self.brand = brand                   # STANY = atrybuty
        self.battery_level = battery_level
        self.is_on = False

    def turn_on(self):                       # ZACHOWANIA = metody (nazwy to czasowniki)
        self.is_on = True
        print('Phone turned on.')

    def turn_off(self):
        self.is_on = False
        print('Phone turned off.')

    def make_call(self, number):
        if self.is_on:
            print(f'Calling {number}...')
            self.battery_level -= 5
        else:
            print('Turn the phone on first!')

    def charge(self):
        self.battery_level = 100
        print('Battery charged to 100%.')

    def show_info(self):
        status = 'on' if self.is_on else 'off'
        print(f'{self.brand}, battery {self.battery_level}%, phone is {status}')


my_phone = Phone('Samsung', 60)
my_phone.show_info()
my_phone.make_call('555-123-456')
my_phone.turn_on()
my_phone.make_call('555-123-456')
my_phone.charge()
my_phone.show_info()
my_phone.turn_off()
