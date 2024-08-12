from turtle import Turtle,Screen



class Ball(Turtle):
    """#创建一个画笔作为球从画布中间随机角度 朝随机xy方向发射 """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(0)
        self.penup()
        self.color("red")
        self.x_angle=5
        self.y_angle=5
        self.move_speed =0.08

    
    def move(self):
        nwe_x=self.xcor()+self.x_angle
        nwe_y=self.ycor()+self.y_angle
        self.goto(nwe_x,nwe_y)
        
    def bounce_y(self):
        self.y_angle *= -1 
        self.move_speed *= 0.9
    def bounce_x(self):
        self.x_angle *= -1 
        self.move_speed *= 0.9
                
   
        
    def goto_s(self):
        self.goto(0,0)
        self.x_angle *= -1 
        self.move_speed = 0.1
    
    