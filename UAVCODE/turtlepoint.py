import turtle 

def setturtle():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.pensize(4)

def point(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x, y)