from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        x_cor = 0
        y_cor = 0 

        for next_turtle in range(3):
            next_turtle = Turtle(shape="square")
            next_turtle.color("white")
            next_turtle.penup()
            next_turtle.goto(x_cor, y_cor)
            self.all_turtles.append(next_turtle)
            x_cor -= 20

    def move(self):
        for seg_num in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[seg_num-1].xcor()
            new_y = self.all_turtles[seg_num-1].ycor()
            self.all_turtles[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)   

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

