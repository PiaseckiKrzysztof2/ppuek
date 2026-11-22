# Zadanie 7-2.4 - Plan posiłków
# Co robi: tabela 7x3: wiersz = dzień, kolumny = śniadanie, obiad, kolacja.
#          Program wypisuje plan na cały tydzień: nazwa dnia i posiłki po przecinku.

meal_plan = [
    ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
    ["Pancakes", "Sandwich", "Steak"],
    ["Smoothie", "Chicken Wrap", "Salmon"],
    ["Eggs", "Pasta", "Soup"],
    ["Toast", "Burrito", "Pizza"],
    ["Cereal", "Salad", "Fish Tacos"],
    ["Bagel", "Rice and Beans", "Stir-fry"]
]


def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n - 1]


def day_meal_plan(meal_plan, day_number):
    return ", ".join(meal_plan[day_number - 1])    # join - skleja posiłki, wstawiając ", "


print('WEEKLY MEAL PLAN')
print('(Breakfast, Lunch, Dinner)')
print('==========================')
for day in range(1, len(meal_plan) + 1):           # dni 1..7
    print(f'{weekday(day)}: {day_meal_plan(meal_plan, day)}')
