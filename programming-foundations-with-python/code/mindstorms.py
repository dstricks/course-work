import turtle

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(2)

    for i in range(0,4):
        brad.forward(100)
        brad.right(90)
        i = i + 1

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_initials():
    david = turtle.Turtle()
    david.shape("classic")
    david.color("white")

    david.penup()
    david.setx(-150)
    david.pendown()
    david.circle(120,180)
    david.left(90)
    david.forward(240)
    david.penup()
    david.home()
    david.setx(50)
    david.sety(240)
    david.left(180)
    david.pendown()
    david.circle(70,160)
    david.circle(-70,160)

window = turtle.Screen()
window.bgcolor("red")

#draw_square()
#draw_circle()
draw_initials()

window.exitonclick()