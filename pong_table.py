from turtle import Turtle, Screen
from random import randint
from time import sleep


class Paddle:

    def __init__(self, position):
        super().__init__()
        self.my_paddle = Turtle(shape="square")
        self.my_paddle.color("white")
        self.my_paddle.penup()
        self.my_paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.my_paddle.goto(position)

    def up(self):
        self.new_y = self.my_paddle.ycor() + 20
        self.my_paddle.goto(self.my_paddle.xcor(), self.new_y)

    def down(self):
        self.new_y = self.my_paddle.ycor() - 20
        self.my_paddle.goto(self.my_paddle.xcor(), self.new_y)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 20
        self.y_move = 20

    def move(self):
        x_cordinate = self.xcor() + self.x_move
        y_cordinate = self.ycor() + self.y_move
        self.goto(x_cordinate, y_cordinate)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()


screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Pong Table")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "q")
screen.onkey(left_paddle.down, "a")

game_on = True
while game_on:
    sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with upper and lower wall
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    # Detect ball collision with the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when ball goes past the right paddle
    if ball.xcor() > 380:
        ball.reset()

    # Detect when the ball goes pastthe left paddle
    if ball.xcor() < -380:
        ball.reset()

screen.exitonclick()