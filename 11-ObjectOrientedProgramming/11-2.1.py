# Zadanie 11-2.1 - Metoda __str__ (przykład z treści)
# Co robi: klasa Car ma metodę __str__, która mówi, jak wypisać obiekt.
#          Dzięki temu print(my_car) wypisuje "2021 Toyota Corolla".


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):                       # __str__ - zwraca NAPIS, który pokaże print(obiekt)
        return f"{self.year} {self.brand} {self.model}"


my_car = Car("Toyota", "Corolla", 2021)

print(my_car)                                # Python sam wywołuje my_car.__str__()
