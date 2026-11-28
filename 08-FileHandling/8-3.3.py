# Zadanie 8-3.3 - Wzorce wyrażeń regularnych (regex101)
# Co robi: w treści zadania wzorce testuje się na stronie regex101.com.
#          Tutaj te same wzorce są sprawdzone w Pythonie: dla każdego wypisuje,
#          co znalazł w tekście (daty, telefony, liczby z przecinkiem, imiona, liczby).

import re                                    # moduł do wyrażeń regularnych

text = ("Alice was born on March 12, 1992. Her brother, John, was born on June 5, 1988. "
        "They have a mutual friend named Mike, whose phone number is 555-123-4567. "
        "In their hometown, which has a population of 1,234 or 1,235 people, a holiday "
        "festival is held every year on December 25. Alice works in an office with 30 "
        "employees. Her phone number is 555-765-4321.")

patterns = {
    'Dates (month day, year)': r'[A-Z][a-z]+ \d{1,2}, \d{4}',   # [A-Z] wielka litera, \d cyfra, {4} dokładnie 4 razy
    'Phone numbers XXX-XXX-XXXX': r'\d{3}-\d{3}-\d{4}',
    'Numbers like 1,234': r'\d{1,3}(?:,\d{3})+',                # + - co najmniej raz
    'Words starting with a capital': r'\b[A-Z][a-z]+\b',        # \b - granica słowa
    'Whole numbers': r'\b\d+\b',
}

for description, pattern in patterns.items():
    print(f'{description}: {pattern}')
    print('   ', re.findall(pattern, text))   # findall - lista WSZYSTKICH dopasowań
