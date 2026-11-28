# Zadanie 11-1.1 - Klasa Student z trzecim atrybutem (student.py)
# Co robi: klasa Student opisuje studenta: imię, wiek i (dodany) kierunek studiów.
#          Program tworzy trzech studentów, ustawia ich dane i wypisuje listę.


class Student():                             # class - definicja KLASY, czyli "przepisu" na obiekty
    def __init__(self):                      # __init__ - konstruktor: wykonuje się przy tworzeniu obiektu
        self.name = ""                       # self.coś - ATRYBUT, czyli dana należąca do obiektu
        self.age = 0
        self.major = ""                      # trzeci, dodany atrybut


def main():
    student1 = Student()                     # tworzenie OBIEKTU na podstawie klasy
    student2 = Student()
    student3 = Student()

    student1.name = "Dominic"                # obiekt.atrybut = wartość
    student1.age = 19
    student1.major = "Computer Science"
    student2.name = "Olivia"
    student2.age = 21
    student2.major = "Economics"
    student3.name = "Kacper"
    student3.age = 20
    student3.major = "Mathematics"

    print('LIST OF STUDENTS')
    print('================')
    for student in [student1, student2, student3]:
        print(f'{student.name}, {student.age} years old, {student.major}')


if __name__ == "__main__":
    main()
