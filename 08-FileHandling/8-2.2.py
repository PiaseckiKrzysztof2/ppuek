# Zadanie 8-2.2 - Siedem cudów świata do pliku
# Co robi: sortuje alfabetycznie listę siedmiu cudów świata i zapisuje je do pliku
#          seven_wonders.txt, każdy w osobnej linijce.

seven_wonders = [
    "Great Wall of China",
    "Petra",
    "Christ the Redeemer",
    "Machu Picchu",
    "Chichen Itza",
    "Roman Colosseum",
    "Taj Mahal"
]

file_name = 'seven_wonders.txt'

seven_wonders = sorted(seven_wonders)        # alfabetycznie

with open(file_name, 'w') as file:
    for item in seven_wonders:
        file.write(item + '\n')              # każdy cud w nowej linijce

print(f'Seven Wonders of the World have been written to {file_name}.')
