from turtle import Turtle,Screen
from random import randint


class Ball(Turtle):
    """#创建一个画笔作为球从画布中间随机角度 朝随机xy方向发射 """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(0)
        self.penup()
        self.color("red")
        self.shapesize(0.5,0.5)
        self.angle=[]

        
    def left_create(self):
        random_y=randint(-280,280)
        # print(random_y)
        self.goto(0,random_y)
        angle_Left=randint(100,250)
        # print(angle_Left)
        self.seth(angle_Left)

    
    def reft_create(self):
        random_y=randint(-280,280)
        # print(random_y)
        self.goto(0,random_y)
        angle_right=randint(290,390)
        # print(angle_right)
        self.seth(angle_right)
    
    def reft_left_create(self):
        a=randint(0,1)
        print(a)
        print("1应该右发球")
        if a == 1:
            self.reft_create()
            print("右发球")
        else:
            self.left_create()
            print("左发球")
            
    def rebound(self):
        angle = self.heading()
        angle -= 270
        self.seth(angle)
        
    def goto_s(self):
        self.goto(0,0)
    
    