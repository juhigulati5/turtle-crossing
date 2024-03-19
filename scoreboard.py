from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-275, 250)
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_score(self):
        self.level +=1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)