# Zadanie 7-1.8 - Lista gier
# Co robi: sortuje listę gier alfabetycznie i wypisuje ją ponumerowaną (1., 2., ...),
#          używając pętli while.

computer_games = [
    "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
    "League of Legends", "Valorant", "Grand Theft Auto V",
    "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

sorted_games = sorted(computer_games)         # sorted - nowa, posortowana lista

i = 0
while i < len(sorted_games):                  # while - dopóki są jeszcze gry
    print(f'{i + 1}. {sorted_games[i]}')      # i + 1, żeby numerować od 1, a nie od 0
    i += 1                                    # bez tego pętla nieskończona
