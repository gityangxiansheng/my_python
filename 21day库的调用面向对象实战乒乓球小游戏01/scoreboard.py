from turtle import Turtle 
import time
ALIGN="center"
FONT=("Arial",36,"normal")
GAME_OVER_FONT=("Arial",36,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_us1=0
        self.score_us2=0
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.color("white")
        self.得分=""
    
    def scores_1(self):
        self.scores_us1()
        self.scores_us2()
        
    def us1_scores(self):
     
        self.得分="玩家1得分"
        self.over()
        self.screen.update()
        time.sleep(3)
        self.clear()
        self.score_us1 += 1
        self.scores_us1()
        
    def us2_scores(self):
        self.得分="玩家2得分"
        self.over()
        self.screen.update()
        time.sleep(3)
        self.clear()
        self.score_us2 += 1
        self.scores_us2()
        
    def scores_us1(self):
        self.goto(-50,250)
        self.write(f"{self.score_us1}",align=ALIGN,font=FONT)
        
    def scores_us2(self):
        self.goto(50,250)
        self.write(f"{self.score_us2}",align=ALIGN,font=FONT)
        
    def over(self):
        self.goto(0,0)
        self.write(f"{self.得分}",align=ALIGN,font=GAME_OVER_FONT)
