# Zadanie 9-5.12 - Odwracanie tekstu stosem
# Co robi: funkcja reverse_text kładzie każdy znak napisu na stos, a potem zdejmuje je
#          po kolei - wychodzą od końca, więc tekst jest odwrócony. Tekst wpisuje użytkownik.

import queue


def reverse_text(text):
    stack = queue.LifoQueue()
    for char in text:
        stack.put(char)                      # znak po znaku na stos
    result = ''
    while not stack.empty():
        result += stack.get()                # zdejmujemy od ostatniego
    return result


text = input('Enter text: ')
print('Reversed:', reverse_text(text))
