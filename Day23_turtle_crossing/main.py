import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("DS TURTLE CROSSING")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    scoreboard.update_display()
    screen.update()

    #Detecting finish line
    if player.ycor() > 280:
        scoreboard.levelup()
        player.restart()
        scoreboard.update_display()

screen.exitonclick()