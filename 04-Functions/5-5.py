# Rysuje każdą figurę dwa razy w różnych miejscach
import figures
import turtle

# ustawienie ekranu
window = turtle.Screen()
window.bgcolor("lightgreen")

# żółw z modułu figures
pen = figures.pen
pen.speed(5)


def move_to(x, y):
    # przesuwa żółwia bez rysowania
    pen.penup()  # podnosi pisak
    pen.goto(x, y)
    pen.pendown()  # opuszcza pisak


# rysowanie figur
move_to(-250, 200)
figures.draw_square(100)
move_to(-250, -50)
figures.draw_square(60)

move_to(-50, 100)
figures.draw_triangle(100)
move_to(-50, -150)
figures.draw_triangle(70)

move_to(120, 200)
figures.draw_rectangle(150, 80)
move_to(120, -50)
figures.draw_rectangle(80, 120)

# chowam żółwia i kończę
pen.hideturtle()
window.mainloop()
