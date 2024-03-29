from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.back_to_start()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def back_to_start(self):
        self.goto(STARTING_POSITION)
