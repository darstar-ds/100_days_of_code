from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("DS Pong Game")
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball((0,0))
ball_jump = 5
scoreboard = Scoreboard()
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
    ball.move(y_up_or_down, x_left_or_right, ball_jump)
    scoreboard.display()
    screen.update()

    #Detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        y_up_or_down *= -1

    #Detecting collision with r_paddle or with l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
        x_left_or_right *= -1
        # ball_speed -= 0.01
        ball_jump += 1

    #Detecting a missed ball by r_paddle
    if ball.xcor() > 400:
        ball.reset()
        x_left_or_right *= -1
        scoreboard.l_score_point()
    

    #Detecting a missed ball by l_paddle
    if ball.xcor() < -400:
        ball.reset()
        x_left_or_right *= -1
        scoreboard.r_score_point()



screen.exitonclick()