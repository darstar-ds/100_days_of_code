from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__(self)
        
    def display(self, score):
        self.write(f"Score: {}", align="center")
    
    def update_display(self, score):
        self.clear()
        self.display(score)