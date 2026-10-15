from turtle import *
from colorsys import *
setposition(0, -100)
tracer(10)
bgcolor("black")
h = 0
for i in range(90):
    h += 0.0015
    color(hsv_to_rgb(h , 1, 1))
    lt(50)
    for j in range(7):
        fd(340)
        lt(100)
        circle(5)
    right(90)
    circle(10)
    hideturtle()
done()