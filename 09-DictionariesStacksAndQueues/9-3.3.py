# Zadanie 9-3.3 - Poprawność nawiasów
# Co robi: funkcja brackets_ok sprawdza stosem, czy nawiasy (), [], {} w wyrażeniu
#          są poprawnie otwarte i zamknięte. Program sprawdza 3 wyrażenia.

import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"   # brackets ok
expression2 = "[(2+3]/4)"                   # brackets not correct
expression3 = "(2-3*4+(5/6)"                # brackets not correct

pairs = {')': '(', ']': '[', '}': '{'}       # zamykający -> pasujący otwierający


def brackets_ok(expression):
    stack = queue.LifoQueue()
    for char in expression:
        if char in '([{':                    # nawias otwierający -> na stos
            stack.put(char)
        elif char in ')]}':                  # nawias zamykający
            if stack.empty():                # nie ma czego zamknąć
                return False
            if stack.get() != pairs[char]:   # zdejmij ostatni otwarty - musi pasować
                return False
    return stack.empty()                     # na końcu nic nie może zostać otwarte


for expression in [expression1, expression2, expression3]:
    if brackets_ok(expression):
        print(f'{expression} -> brackets are OK')
    else:
        print(f'{expression} -> brackets are NOT correct')
