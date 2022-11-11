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
cars = []
create_counter = 0

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
    
    #Creating cars:
    create_counter += 1
    if create_counter % 6 == 0:
        new_car = CarManager()
        cars.append(new_car)

    #Detecting collision with a car:
    for car in cars:
        if car.distance(player) < 20:
            scoreboard.gameover()
            game_is_on = False
        #Moving cars forward
        car.move(scoreboard.user_level*1.5)
        # Removing cars that hissed by the window
        if car.xcor() < -350:
            cars.remove(car)



screen.exitonclick()