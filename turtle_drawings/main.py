from turtle import Turtle, Screen
import random
import colorgram

screen = Screen()
screen.colormode(255)
# screen.delay(55)

def get_rgb(color_pos):
    rgb = colors[color_pos].rgb
    return rgb

colors = colorgram.extract('image.jpg', 12)
print(colors)
print(len(colors))
colors_list = []

for pos in range(len(colors)):
    next_color = get_rgb(pos)
    # print(next_color)
    r = next_color[0]
    g = next_color[1]
    b = next_color[2]
    color_tuple = (r, g, b)
    # print(color_tuple)
    colors_list.append(color_tuple)
    
print(colors_list)


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("DarkGrey")

# def random_color():
#     r = random.randint(1,255)
#     g = random.randint(1,255)
#     b = random.randint(1,255)
#     color = (r, g, b)
#     return color

# Challenge 1 - a rectangle
# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.rt(90)

# Challenge 2 - dashed line
# for _ in range(15):
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(5)    
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(5)

# Challenge 3 - triangle2octagon in random color
# for sides_no in range(3,11):
#     turn_angle = 360/sides_no
#     r = random.randint(1,255)
#     g = random.randint(1,255)
#     b = random.randint(1,255)
#     print(f"r= {r}, g= {g}, b= {b}")
#     timmy_the_turtle.pencolor(r,g,b)
#     timmy_the_turtle.pendown()
#     for _ in range(sides_no):
#         timmy_the_turtle.forward(60)
#         timmy_the_turtle.right(turn_angle)

# Challenge 4 - random walk
# for _ in range(100):
#     r = random.randint(1,255)
#     g = random.randint(1,255)
#     b = random.randint(1,255)
#     timmy_the_turtle.pencolor(r,g,b)
#     timmy_the_turtle.speed = 1
#     timmy_the_turtle.pensize(10)
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.rt(90*random.randint(1,4))


# Challenge 5 - Spirograph
# circles_no = 50
# turn_angle = 360 / circles_no
# for _ in range(circles_no):
#     timmy_the_turtle.pencolor(random_color())
#     timmy_the_turtle.circle(100)
#     timmy_the_turtle.rt(turn_angle)

# Challenge 6 - Hirst painting

screen.exitonclick()
