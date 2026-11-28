# Zadanie 8-1.8 - Liczba słów w pliku
# Co robi: wypisuje zabawny tekst z pliku pets.txt i liczy, ile jest w nim słów.

words = 0
with open('pets.txt', 'r') as file:
    for line in file:
        print(line, end="")
        words += len(line.split())           # split - lista słów w linijce, len - ile ich jest

print()
print('Number of words:', words)
