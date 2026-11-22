# Oblicza wyrażenie z dodawaniem i odejmowaniem
def f(expression):
    result = 0
    sign = 1  # 1 dodawanie, -1 odejmowanie
    for char in expression:
        if char == '+':
            sign = 1
        elif char == '-':
            sign = -1
        else:
            result += sign * int(char)  # dodaję cyfrę z odpowiednim znakiem
    return result


def main():
    for expr in ["2+3", "3+8+1", "2+3-4+5-0"]:
        print(f'f("{expr}") returns {f(expr)}')


if __name__ == "__main__":
    main()
