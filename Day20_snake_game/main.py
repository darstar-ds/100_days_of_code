from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("DS Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
# print(snake)
# print(all_turtles)    
# screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

score = 0
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.display(score)

    #Detecting collision with food
    if snake.head.distance(food) < 15:
        score += 1
        food.refresh()
        snake.extend()
        scoreboard.update_display(score)

    #Detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.gameover()
        
    #Detecting collision with tail
    for turtle in snake.all_turtles[1:]:
        if snake.head.distance(turtle) < 10:
            game_is_on = False
            scoreboard.gameover()
    
screen.exitonclick()