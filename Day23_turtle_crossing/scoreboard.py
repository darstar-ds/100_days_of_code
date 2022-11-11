from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("grey")
        self.penup()
        self.hideturtle()
        self.user_level = 1

    def display(self):
        self.goto(-280, 250)
        self.write(f"LEVEL: {self.user_level}", align="left", font=FONT)
    
    def update_display(self):
        self.clear()
        self.display()

    def levelup(self):
        self.user_level += 1
        self.update_display()

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=("Courier", 36, "bold"))
