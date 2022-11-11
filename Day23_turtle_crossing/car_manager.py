from turtle import Turtle
from scoreboard import Scoreboard
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLORS[random.randint(0,5)])
        self.shape("square")
        self.resizemode("user")
        self.shapesize(1,2)
        self.penup()
        self.goto(300, random.randint(-250, 250))

    def move(self, speed):
        new_x = self.xcor() - MOVE_INCREMENT*speed
        self.goto(new_x, self.ycor())

