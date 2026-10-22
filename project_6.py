import colorsys
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(700,700)

t = turtle.Turtle()
t.speed(0)
t.width(1)

for i in range(200):
    color = colorsys.hsv_to_rgb(i/200 ,1,1)
    t.pencolor(color)
    t.circle(10 + i * 0.8)
    t.left(20)
    t.forward(i *0.15)

turtle.done()
