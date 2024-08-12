from turtle import Turtle 

FONT = ("Courier", 24, "normal")
VOER_FONT = ("Courier", 60, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-200,250)
        self.hideturtle()
        self.color("black")
        self.scores()
        
    def scores(self):
        self.write(f"当前关卡：{self.level}",align="center",font=FONT)
    
    def scores_promotion(self):
        self.level += 1
        self.clear()
        self.scores()
        
    def over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=VOER_FONT)

