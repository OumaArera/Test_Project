from turtle import Turtle, Screen
from random import randint
from time import sleep

#Constants
S_POSITION = [(0, 0), (0, -20), (0, -40)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class SnakeXenzia:
    '''
    Creates the snake and keeps increasing it
    '''

    def __init__(self):
        self.my_snake = []
        self.create_snake()
        self.head = self.my_snake[0]

    def create_snake(self):
        '''
        Creates the snake

        '''
        for snake_position in S_POSITION:
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.speed("slowest")
            segment.goto(snake_position)
            self.my_snake.append(segment)

    def add_segment(self, position):
        '''
        Creates new segment of the snake at the last
        the tail of the snake
        '''
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.speed("slowest")
        segment.goto(self.my_snake[-1].position())
        self.my_snake.append(segment)

    def extend_snake(self):
        '''
        Extends the first snake anytime the snake eats food

        '''
        self.add_segment(self.my_snake[-1].position())

    def snake_move(self):
        '''
        makes the snake to move
        '''

        for snake_num in range(len(self.my_snake) - 1, 0, -1):
            new_x = self.my_snake[snake_num - 1].xcor()
            new_y = self.my_snake[snake_num - 1].ycor()
            self.my_snake[snake_num].goto(new_x, new_y)
        self.head .forward(MOVE_DISTANCE)

    def up(self):
        '''
        turns the snake up using the down arrow key
        '''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        '''
        Turns the snake down using the up arrow key
        '''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def right(self):
        '''
        Turns the snake right using the right arrow key
        '''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def left(self):
        '''
        turns the snake left using the left arrow key
        :return:
        '''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


class Food(Turtle):
    '''
    Creates the food for the snake
    '''

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid= 1.5, stretch_len= 1.5)
        self.color('green')
        self.speed('fastest')
        self.refresh_food()

    def refresh_food(self):
        '''
        Creates food for the snake and onces it has eaten it,
        the food to another random location on the screen
        '''
        x_axis = randint(-350, 350)
        y_axis = randint(-350, 350)
        self.goto(x=x_axis, y=y_axis)

class ScoreBoard(Turtle):
    '''
    Keeps track of the player's score
    '''

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(x=0, y=370)
        self.score = 0
        self.hideturtle()
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        '''
        Updates the scoreboard
        '''
        self.write(f"Score = {self.score}", align="center", font=("Arial", 12, "normal"))

    def game_over(self):
        '''
        Displays GAME OVER when a player loses
        '''
        self.goto(x=0, y=0)
        self.write(f"GAME OVER! \n\nYour Score is {self.score}", align="center", font=("Arial", 12, "normal"))

    def increase_scores(self):
        '''
        Keeps increasing the score anytime the snake eats the food
        '''
        self.score += 1
        self.clear()
        self.update_scoreboard()



screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Xenzia")
screen.tracer(0)

#Thuol is the name of snake in my first language :)
#From the SnakeXenzia class, we create a snake that I have called thuol
#From the Food class, we create food
#Finally from the SCoreBoard class, we create the score
thuol = SnakeXenzia()
food = Food()
score = ScoreBoard()

#We instruct the screen to respond to certain commands when pressed on the screen
screen.listen()
screen.onkey(thuol.up, "Up")
screen.onkey(thuol.down, "Down")
screen.onkey(thuol.right, "Right")
screen.onkey(thuol.left, "Left")

game_on = True
while game_on:
    screen.update()
    sleep(0.05)
    thuol.snake_move()

    #Detect collision with food
    if thuol.head.distance(food) < 25:
        thuol.extend_snake()
        food.refresh_food()
        score.increase_scores()

    if thuol.head.xcor() > 390 or thuol.head.xcor() < -390 or thuol.head.ycor() > 390 or thuol.head.ycor() < -390:
        game_on = False
        score.game_over()

    #Detect collision with any part of the body
    for segment in thuol.my_snake[1:]:
        if thuol.head.distance(segment) < 10:
            game_on = False
            score.game_over()


#This ensures the screen doesn't varnish unless instructed
screen.exitonclick()