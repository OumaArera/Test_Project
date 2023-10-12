from turtle import Turtle, Screen
from random import randint
from time import sleep

class Paddle(Turtle):


    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.penup()
        self.goto(position)


    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 20
        self.y_move   = 20
        self.velocity = 0.1



    def move(self):
        x_cordinate = self.xcor() + self.x_move
        y_cordinate = self.ycor() + self.y_move
        self.goto(x_cordinate, y_cordinate)


    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1
        self.velocity *= 0.9


    def reset(self):
        self.goto(0,0)
        self.velocity = 0.1
        self.bounce_x()

class ScoreBoard(Turtle):

    def __init__(self, location):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(location)
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()



screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Pong Table")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
left_score = ScoreBoard((-200, 350))
right_score = ScoreBoard((200, 350))

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

    #detect collision with upper and lower wall
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()


    #Detect ball collision with the paddles
    if ball.distance(right_paddle) < 50 or ball.distance(left_paddle) < 50:
        ball.bounce_x()

    #Detect when ball goes past the right paddle
    if ball.xcor() > 380:
        left_score.increase_score()
        ball.reset()

    #Detect when the ball goes pastthe left paddle
    if ball.xcor() < -380:
        right_score.increase_score()
        ball.reset()

screen.exitonclick()