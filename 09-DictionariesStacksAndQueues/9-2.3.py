# Zadanie 9-2.3 - Nieobecni studenci
# Co robi: odejmuje zbiór obecnych od zbioru wszystkich studentów,
#          żeby dostać nieobecnych (John, Sara).

all_students = {"Alice", "John", "Sara", "Bob"}
attended_students = {"Alice", "Bob"}

absent_students = all_students - attended_students      # - różnica: są w pierwszym, nie ma w drugim
print(absent_students)
