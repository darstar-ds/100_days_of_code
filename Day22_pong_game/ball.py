from turtle import Turtle

# BALL_JUMP = 5

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(position)

    def move(self, y_up_or_down, x_left_or_right, ball_jump):
        new_x = self.xcor() + ball_jump*x_left_or_right
        new_y = self.ycor() + ball_jump*y_up_or_down
        self.goto(new_x, new_y)

    def reset(self):
        self.goto(0,0)
