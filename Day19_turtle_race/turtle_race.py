from turtle import Turtle, Screen
import turtle
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=480)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = turtle.textinput(title="Make your bet", prompt="Who is gonna to win the race? Bet the color: ").lower
all_turtles = []
turtles_names = []
for t_color in colors:
    turtles_names.append("tim_" + t_color)

x_cor = -230
y_cor = -100 
t_color = 0   
for col_turtle in turtles_names:
    col_turtle = Turtle(shape="turtle")
    all_turtles.append(col_turtle)
    col_turtle.color(colors[t_color])
    col_turtle.penup()
    col_turtle.goto(x_cor, y_cor)
    y_cor += 40
    t_color += 1

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle_boy in all_turtles:
        if turtle_boy.xcor() > 230:
            is_race_on = False
            winning_color = turtle_boy.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} color is the winner.")
            else:
                print(f"You've lost! The {winning_color} color is the winner.")
        rand_distance = random.randint(0,10)
        turtle_boy.forward(rand_distance)


# print(len(all_turtles))    
# print(all_turtles)
screen.exitonclick()
