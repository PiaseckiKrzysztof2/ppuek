# Zadanie 9-5.14 - Obsługa klientów w urzędzie
# Co robi: menu: 1 - nowy klient dostaje kolejny numerek i staje na końcu kolejki,
#          2 - obsługujemy klienta z początku kolejki, 0 - koniec.

import queue

customers = queue.Queue()                    # kolejka FIFO
next_ticket = 1                              # kolejny numerek do wydania

while True:
    print('1. New customer (take a ticket)')
    print('2. Serve next customer')
    print('0. Quit')
    option = input('Select an option: ')

    if option == '1':
        customers.put(next_ticket)
        print(f'Your ticket number is {next_ticket}. Please wait.')
        next_ticket += 1
    elif option == '2':
        if customers.empty():
            print('No customers in the queue.')
        else:
            print(f'Customer with ticket {customers.get()} please come to the desk.')
    elif option == '0':
        break
    print()
