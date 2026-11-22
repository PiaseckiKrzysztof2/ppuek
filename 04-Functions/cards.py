# Moduł: maskowanie numeru karty kredytowej
def hide(card_number):
    # pierwsze 2 znaki, gwiazdki i ostatnie 4 znaki
    hidden_count = len(card_number) - 6
    return card_number[:2] + '*' * hidden_count + card_number[-4:]
