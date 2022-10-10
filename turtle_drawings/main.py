from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("DarkGrey")

# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.rt(90)

for _ in range (15):
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(5)    
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(5)

screen = Screen()
screen.exitonclick()
