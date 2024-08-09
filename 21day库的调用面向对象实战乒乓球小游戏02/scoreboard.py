from turtle import Turtle 
import time
ALIGN="center"
FONT=("Arial",36,"normal")
GAME_OVER_FONT=("Arial",36,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
   
    def prints(self):
        self.goto(-100,230)
        self.write(f"{self.l_score}",align=ALIGN,font=FONT)
        self.goto(100,230)
        self.write(f"{self.r_score}",align=ALIGN,font=FONT)
    
    def l_scoress(self):
        self.clear()
        self.l_score += 1  
        self.prints()    
    
    def r_scoress(self):
        self.clear()
        self.r_score += 1  
        self.prints()  
        
        
    # def us2_scores(self):
    #     self.得分="玩家2得分"
    #     self.over()
    #     self.screen.update()
    #     time.sleep(3)
    #     self.clear()
    #     self.score_us2 += 1
    #     self.scores_us2()
        
    # def scores_us1(self):
    #     self.goto(-50,250)
    #     self.write(f"{self.score_us1}",align=ALIGN,font=FONT)
        
    # def scores_us2(self):
    #     self.goto(50,250)
    #     self.write(f"{self.score_us2}",align=ALIGN,font=FONT)
        
    # def over(self):
    #     self.goto(0,0)
    #     self.write(f"{self.得分}",align=ALIGN,font=GAME_OVER_FONT)
