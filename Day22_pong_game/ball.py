from turtle import Turtle

BALL_JUMP = 5

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(position)

    def move(self, y_up_or_down, x_left_or_right):
        new_x = self.xcor() + BALL_JUMP*x_left_or_right
        new_y = self.ycor() + BALL_JUMP*y_up_or_down
        self.goto(new_x, new_y)
