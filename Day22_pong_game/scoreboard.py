from turtle import Turtle
FONT = ('Courier', 60, 'normal')
ALIGNEMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def display(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=FONT)
    
    def update_display(self):
        self.clear()
        self.display()

    def l_score_point(self):
        self.l_score += 1
        self.update_display()
    
    def r_score_point(self):
        self.r_score += 1
        self.update_display()
