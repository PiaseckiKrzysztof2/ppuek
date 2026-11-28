# Zadanie 9-4.2 - Kolejka plików do drukowania
# Co robi: menu do drukarki: 1 dodaje plik na koniec kolejki, 2 drukuje plik z początku
#          kolejki (albo informuje, że kolejka jest pusta), 0 kończy program.

import queue

files_to_print = queue.Queue()

while True:
    print('1. Add file to print')
    print('2. Print file')
    print('0. Quit')
    menu = input('Select an option: ')

    if menu == '1':
        file_name = input('Enter file name to print: ')
        files_to_print.put(file_name)        # na koniec kolejki
        print(f'File {file_name} added to the print queue.')

    elif menu == '2':
        if not files_to_print.empty():
            file_to_print = files_to_print.get()     # z początku kolejki
            print(f'File {file_to_print} is currently being printed. Please wait!')
        else:
            print('The print queue is empty.')

    elif menu == '0':
        break
    print()
