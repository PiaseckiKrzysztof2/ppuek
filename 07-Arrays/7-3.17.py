# Zadanie 7-3.17 - Krotka od tyłu
# Co robi: wypisuje krotkę (10, 20, 30, 40, 50) normalnie i w odwrotnej kolejności.

numbers = (10, 20, 30, 40, 50)                # krotka - nawiasy okrągłe, nie można jej zmieniać

reversed_numbers = numbers[::-1]              # [::-1] - od tyłu (działa jak w napisach i listach)

print('Tuple:', ','.join(str(n) for n in numbers))
print('Reverse order:', ','.join(str(n) for n in reversed_numbers))
