# Zadania 11-3.1 do 11-3.6 - Moduł tv (klasa TV)
# Co robi: MODUŁ z klasą TV opisującą telewizor. Klasa jest rozbudowywana krok po kroku
#          w zadaniach 11-3.1 ... 11-3.6 - przy każdej części jest numer zadania, w którym doszła.
#          Używają go programy 11-3.1.py ... 11-3.6.py (w treści zadania: tv_show.py).


class TV:
    def __init__(self):
        self.is_on = False                   # 11-3.1: na początku telewizor wyłączony
        self.channel_no = 1                  # 11-3.2: na początku kanał 1
        self.channels = []                   # 11-3.4: lista nazw kanałów, na początku pusta
        self.volume = 0                      # 11-3.6: głośność 0..10, na początku 0

    # 11-3.1
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on:
            status = f'TV is on, channel {self.channel_no}'                  # 11-3.2: numer kanału
            if 1 <= self.channel_no <= len(self.channels):                   # 11-3.5: nazwa, jeśli taki kanał jest
                status += f' ({self.channels[self.channel_no - 1]})'         # - 1, bo kanał 1 to indeks 0
            status += f', volume {self.volume}'                              # 11-3.6: głośność
            print(status)
        else:
            print('TV is off')

    # 11-3.3
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    # 11-3.4
    def set_channels(self, channels_list):
        self.channels = channels_list

    def show_channels(self):
        if len(self.channels) == 0:
            print('Channel list is empty (TV not programmed).')
        else:
            print('Channel list:')
            for number, name in enumerate(self.channels, start=1):    # numeracja od 1
                print(f'{number}. {name}')

    # 11-3.6
    def volume_up(self):
        if self.volume < 10:                 # nie więcej niż 10
            self.volume += 1

    def volume_down(self):
        if self.volume > 0:                  # nie mniej niż 0
            self.volume -= 1
