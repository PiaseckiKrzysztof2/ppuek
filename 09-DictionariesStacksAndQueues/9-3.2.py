# Zadanie 9-3.2 - Przycisk "Wstecz" w przeglądarce (back.py)
# Co robi: symuluje przeglądarkę. Wpisanie adresu otwiera nową stronę, a poprzednia
#          trafia na stos. Wpisanie 0 cofa do ostatnio odwiedzonej strony (zdejmuje ją ze stosu).
#          Gdy stos jest pusty, 0 kończy program.

import queue

visited_websites = queue.LifoQueue()         # stos odwiedzonych stron

visited_websites.put('instagram.com')
visited_websites.put('uek.krakow.pl')
visited_websites.put('microsoft.com')

current_website = ''                         # strona, którą teraz oglądamy

while True:
    website = input('Enter website name (0 for back): ')

    if website == '0':
        if visited_websites.empty():
            break                            # nie ma gdzie się cofnąć -> koniec
        else:
            print('<-- Going back to a previously visited website')
            website = visited_websites.get() # zdejmij ostatnio odwiedzoną stronę
    elif website != "":
        if current_website != '':
            visited_websites.put(current_website)   # obecna strona idzie na stos, żeby móc do niej wrócić
    else:
        continue                             # pusty napis -> pytaj jeszcze raz

    current_website = website
    print('You are currently viewing:', website)
    print()
