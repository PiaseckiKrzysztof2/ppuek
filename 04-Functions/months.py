# Moduł: nazwa miesiąca na podstawie numeru
def month(n):
    names = ['January', 'February', 'March', 'April', 'May', 'June',
             'July', 'August', 'September', 'October', 'November', 'December']
    if 1 <= n <= 12:  # czy numer jest od 1 do 12
        return names[n - 1]  # lista liczy od 0, więc n - 1
    return 'Unknown month'


if __name__ == "__main__":
    print(month(7))
