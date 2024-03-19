import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
FINISH_LINE_Y = 280


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    #Detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
            scoreboard.game_over()



    #Detect turtle reaches top
    if player.ycor() >= FINISH_LINE_Y:
        player.back_to_start()
        car_manager.increase_speed()
        scoreboard.level_score()

screen.exitonclick()