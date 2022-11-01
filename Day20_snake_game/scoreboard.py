from turtle import Turtle
FONT = ('Courier', 14, 'normal')
ALIGNEMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(0,280)
        
    def display(self, score):
        self.write(f"Score: {score}", move=False, align=ALIGNEMENT, font=FONT)
    
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=ALIGNEMENT, font=FONT)

    def update_display(self, score):
        self.clear()
        self.display(score)