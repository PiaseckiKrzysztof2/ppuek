# Test funkcji z modułu converters
import converters  # mój moduł converters

print('### Test converters')
print(f'Three meters is {converters.m_to_cm(3)}cm')
print(f'250 centimeters is {converters.cm_to_m(250)}m')
# .2f czyli 2 miejsca po przecinku
print(f'30 centimeters is {converters.cm_to_inches(30):.2f} inches')
print(f'6 feet 2 inches is {converters.feet_inches_to_cm(6, 2):.2f}cm')
