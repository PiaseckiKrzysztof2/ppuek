# Zadanie 9-1.3 - Słownik z opisem telefonu
# Co robi: tworzy słownik z 6 informacjami o telefonie i wypisuje go pętlą,
#          każdą parę jako "klucz : wartość".

mobile = {
    "OS": "Android",
    "brand": "Samsung",
    "model": "Galaxy A55",
    "memory_GB": 128,
    "screen_inches": 6.6,
    "color": "Black"
}

for key, value in mobile.items():            # items() - pary klucz i wartość
    print(f"{key} : {value}")
