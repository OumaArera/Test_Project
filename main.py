import turtle
from turtle import Turtle, Screen
from random import choice, randint

opuk = Turtle()
turtle.colormode(255)
opuk.shape("arrow")
opuk.color("brown")
opuk.pensize(10)
opuk.speed(100)


# colors = ["RoyalBlue", "SaddleBrown", "Indigo", "MediumBlue", "Black", "Yellow", "Red"]

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color







def turtle_move():

    for steps in range(36):
        opuk.circle(200)
        opuk.right(10)
        opuk.color(random_color())



turtle_move()

screen = Screen()

screen.exitonclick()
