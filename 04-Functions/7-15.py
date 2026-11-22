# Czy w pokoju były naraz co najmniej 3 osoby
def f(detector):
    people = 0
    for sign in detector:
        if sign == '+':
            people += 1  # ktoś wszedł
        elif sign == '-':
            people -= 1  # ktoś wyszedł
        if people >= 3:
            return True  # były 3 osoby naraz
    return False


def main():
    for data in ["+-+++-+---", "+-+-+-+-", "+-++-+--", "+-++-++-+---"]:
        print(f'f("{data}") returns {f(data)}')


if __name__ == "__main__":
    main()
