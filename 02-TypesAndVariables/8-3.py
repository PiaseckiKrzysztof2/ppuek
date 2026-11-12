# A program that converts Celsius to Kelvin and Fahrenheit
celsius = float(input('Enter temperature in Celsius: '))  # Pobiera temperaturę w stopniach Celsjusza
kelvin = celsius + 273.15                                 # Zamienia Celsjusze na Kelwiny
fahrenheit = celsius * 9 / 5 + 32                         # Zamienia Celsjusze na Fahrenheity
print(f'Temperature in Kelvin: {kelvin:.2f}')
print(f'Temperature in Fahrenheit: {fahrenheit:.2f}')