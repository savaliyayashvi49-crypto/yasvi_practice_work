import turtle as tu

t = tu.Turtle()
t.speed(2)
t.hideturtle()

# Screen no color alag rite set karvu pade
screen = tu.Screen()
screen.bgcolor("black")

t.color("white")

length = 320
t.penup()
t.goto(0, -120)
t.pendown()

for i in range(40):
    t.setheading(140)
    t.forward(length)
    t.circle(-length/2, 200)
    t.setheading(60)
    t.circle(-length/2, 200)
    t.forward(length)

    t.penup()
    t.right(10)
    t.forward(length * 0.03)
    t.setheading(0)

    length *= 0.91
    t.pendown()

tu.done()