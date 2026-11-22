# Zadanie 7-1.11 - Raport temperatur
# Co robi: z listy temperatur z marca wypisuje raport: liczbę pomiarów, średnią,
#          temperaturę minimalną i maksymalną oraz liczbę dni z temperaturą ujemną.

temperatures = [
    3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
    4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
    -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]

measurements = len(temperatures)

temp_total = 0                                # schemat SUMY
for temp in temperatures:
    temp_total = temp_total + temp
avg_temp = temp_total / measurements          # średnia = suma / liczba elementów

min_temp = min(temperatures)
max_temp = max(temperatures)

negative_temp = 0                             # schemat LICZNIKA, pętla while po indeksach
i = 0
while i < len(temperatures):
    if temperatures[i] < 0:
        negative_temp += 1
    i = i + 1

print('TEMPERATURE REPORT')
print('Month: March')
print('Number of measurements:', measurements)
print(f'Average temperature in the month: {avg_temp:.2f}')
print('Minimum temperature:', min_temp)
print('Maximum temperature:', max_temp)
print('Number of days with negative temperature:', negative_temp)
