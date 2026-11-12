# A program that prints your height in cm, feet and inches
cm = 170
total_inches = round(cm / 2.54)                                    # Zamienia centymetry na cale
feet = total_inches // 12                                          # Oblicza liczbę stóp
inches = total_inches % 12                                         # Oblicza pozostałe cale
print(f'I am {cm} cm tall, i.e. {feet} feet and {inches} inches')