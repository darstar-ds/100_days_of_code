from turtle import Turtle

FONT = ('Courier', 14, 'normal')
ALIGNEMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('./data.txt', encoding='utf-8', mode='r') as highscore_bank:
            # for line in highscore_bank:
            #     print(line)
            # print(highscore_bank.tell())
            # highscore_bank.seek(0)
            # print(highscore_bank.tell())
            self.highscore = int(highscore_bank.read())
            # print(highscore_bank.tell())
            print(f"High Score: {self.highscore}")
            # self.highscore = int(self.highscore)
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(0,280)
        
    def display(self):
        self.write(f"Score: {self.score}, High Score: {self.highscore}", move=False, align=ALIGNEMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('./data.txt', mode='w') as highscore_bank:
                highscore_bank.write(str(self.highscore))
        self.score = 0
        self.update_display()

    def scoreup(self):
        self.score += 1
            
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=ALIGNEMENT, font=FONT)

    def update_display(self):
        self.clear()
        self.display()