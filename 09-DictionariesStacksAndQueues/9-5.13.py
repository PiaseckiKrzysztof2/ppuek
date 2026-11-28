# Zadanie 9-5.13 - Kalkulator RPN (odwrotna notacja polska)
# Co robi: liczy wyrażenia zapisane w RPN, np. "2 3 + =" (to znaczy 2 + 3).
#          Liczbę kładzie na stos; przy operatorze zdejmuje dwie liczby, liczy i kładzie wynik;
#          przy "=" zdejmuje i wypisuje wynik. Można wpisywać po jednym elemencie albo całą linijkę.
#          Do sprawdzenia: 2 3 + =  ->  5;  2 4 1 + * =  ->  10;  2 3 + 4 5 + * =  ->  45;
#          8 3 1 + / 3 2 - 4 + * =  ->  10

import queue

stack = queue.LifoQueue()
finished = False

while not finished:
    for token in input('> ').replace('–', '-').split():   # split - pozwala wpisać kilka elementów naraz
        if token in '+-*/':
            b = stack.get()                  # najpierw zdejmujemy DRUGĄ liczbę
            a = stack.get()                  # potem pierwszą
            if token == '+':
                stack.put(a + b)
            elif token == '-':
                stack.put(a - b)
            elif token == '*':
                stack.put(a * b)
            else:
                stack.put(a / b)
        elif token == '=':
            print('Result:', stack.get())    # wynik leży na wierzchu stosu
            finished = True
            break
        else:
            stack.put(float(token))          # liczba -> na stos
