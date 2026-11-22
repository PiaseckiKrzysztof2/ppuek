# Moduł z funkcjami rysującymi figury (turtle)
import turtle

# żółw jest tutaj, więc funkcje dostają tylko długość boku
pen = turtle.Turtle()


def draw_square(length):
    # kwadrat
    for i in range(4):
        pen.forward(length)
        pen.right(90)


def draw_triangle(length):
    # trójkąt równoboczny
    for i in range(3):
        pen.forward(length)
        pen.left(120)  # obrót o 120 stopni


def draw_rectangle(length_a, length_b):
    # prostokąt o bokach a i b
    for i in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)
