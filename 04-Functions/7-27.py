# Sprawdza poprawność kodu produktu
def f(product_code):
    if len(product_code) != 4 or not product_code.isdigit():  # czy są same cyfry
        return False
    digits_sum = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    control_digit = int(product_code[3])
    return digits_sum % 7 == control_digit


def main():
    for code in ["1082", "2035", "1114", "7071"]:
        print(f'f("{code}") returns {f(code)}')


if __name__ == "__main__":
    main()
