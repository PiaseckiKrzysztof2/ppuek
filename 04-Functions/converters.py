# Moduł do zamiany jednostek długości

INCH_IN_CM = 2.54  # 1 cal = 2.54 cm
FOOT_IN_INCHES = 12  # 1 stopa = 12 cali


def m_to_cm(n):
    return n * 100


def cm_to_m(n):
    return n / 100


def cm_to_inches(cm):
    # cm na cale
    return cm / INCH_IN_CM


def feet_inches_to_cm(feet, inches):
    # stopy i cale na cm
    total_inches = feet * FOOT_IN_INCHES + inches
    return total_inches * INCH_IN_CM


# wykona się tylko, gdy uruchomię ten plik
if __name__ == "__main__":
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'100cm = {cm_to_inches(100):.2f}in')
    print(f"5ft 11in = {feet_inches_to_cm(5, 11):.2f}cm")
