# Liczba oczek, która wypadła najwięcej razy z rzędu
def f(dice):
    best_value = dice[0]
    best_length = 1
    current_length = 1
    # porównuję z poprzednim rzutem
    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            current_length += 1  # seria trwa dalej
        else:
            current_length = 1  # nowa seria
        if current_length > best_length:
            best_length = current_length
            best_value = dice[i]
    return int(best_value)


def main():
    for rolls in ["5233165554211", "2133"]:
        print(f'f("{rolls}") returns {f(rolls)}')


if __name__ == "__main__":
    main()
