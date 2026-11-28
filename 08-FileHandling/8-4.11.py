# Zadanie 8-4.11 - Potęgi liczb do pliku
# Co robi: dla liczb od 1 do 100 liczy ich kwadrat i sześcian, wypisuje je w formacie
#          liczba,kwadrat,sześcian (np. 3,9,27) i zapisuje to samo do pliku powers.txt.

file_name = 'powers.txt'

with open(file_name, 'w') as file:
    for n in range(1, 101):                  # 1..100 (101 nie wchodzi)
        line = f'{n},{n ** 2},{n ** 3}'      # ** - potęga
        print(line)
        file.write(line + '\n')

print(f'Saved to {file_name}.')
