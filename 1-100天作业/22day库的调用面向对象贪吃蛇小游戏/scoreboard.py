from turtle import Turtle 


   


ALIGN="center"
FONT=("Arial",24,"normal")
GAME_OVER_FONT=("Arial",36,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open(r"C:\Users\Administrator\Desktop\BaiduSyncdisk\python\tanchishe\datass.txt",mode="r",encoding="utf-8") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.color("white")
        self.scores()
    
    def scores(self):
        self.write(f"最高分：{self.high_score}    当前分数：{self.score}",align=ALIGN,font=FONT)
    def f5s(self):
        self.clear()
        self.scores()
    def f5(self):
        self.score=0
        self.f5s()

    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open(r"C:\Users\Administrator\Desktop\BaiduSyncdisk\python\tanchishe\datass.txt",mode="w",encoding="utf-8") as file:
                file.write(str(self.high_score))
            self.f5s()
    
    # def over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align=ALIGN,font=GAME_OVER_FONT)

    def scoress(self):
        self.score += 1
        self.f5s()