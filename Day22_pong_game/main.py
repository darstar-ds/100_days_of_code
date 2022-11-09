from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("DS Pong Game")
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball((0,0))
ball_xcor = ball.xcor()
ball_ycor = ball.ycor()
y_up_or_down = 1
x_left_or_right = 1

screen.update()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    ball.move(y_up_or_down, x_left_or_right)
    screen.update()

    #Detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        y_up_or_down = -1

    
    # scoreboard.gameover()




screen.exitonclick()