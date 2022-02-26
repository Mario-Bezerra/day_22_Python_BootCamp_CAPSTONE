from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.level = 1

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(0,new_y)

    def back_to_origin(self):
        self.goto(STARTING_POSITION)


