# Rysuje kwadrat funkcją z modułu figures
import turtle
import figures

# ustawienie ekranu
window = turtle.Screen()
window.bgcolor("lightgreen")

# żółw z modułu figures
pen = figures.pen
pen.speed(5)

# długość boku
side_length = 100

# rysowanie kwadratu funkcją z modułu
figures.draw_square(side_length)

# chowam żółwia i kończę
pen.hideturtle()
window.mainloop()
