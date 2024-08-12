from turtle import Turtle

STARTING_POSITION_1 = [(-480,40),(-480,20),(-480,0),(-480,-20),(-480,-40)]
STARTING_POSITION_2 = [(480,40),(480,20),(480,0),(480,-20),(480,-40)]
MOVE_DISTINCE = 40
UP = 90
DOWN = 270
class User():
    """创建一个黑色的画布 然后中间有一条虚线"""
    def __init__(self):
        self.user_1=[]
        self.user_2=[]
        self.create_us_1()
        
        
    def create_us_1(self):
        for position1 in STARTING_POSITION_1:
            tim =Turtle()
            tim.goto(position1)
            tim.color("white")
            tim.shape("square")
            tim.penup()
            tim.setheading(UP)
            self.user_1.append(tim)
        self.create_us_2()
            
    def create_us_2(self):        
        for position2 in STARTING_POSITION_2:
            tim =Turtle()
            tim.goto(position2)
            tim.penup()
            tim.color("white")
            tim.shape("square")
            tim.setheading(UP)
            self.user_2.append(tim)
            
    # def move(self,user_x_list):
    #     for tim_num in user_x_list:
    #         tim_num.forward(MOVE_DISTINCE)

    
    def up(self):
        for tim_num in self.user_1:
            tim_num.forward(MOVE_DISTINCE)
            
    def down(self):
        for tim_num in self.user_1:
            tim_num.backward(MOVE_DISTINCE)
            
    def up_2(self):
        for tim_num in self.user_2:
            tim_num.forward(MOVE_DISTINCE)
            
    def down_2(self):
        for tim_num in self.user_2:
            tim_num.backward(MOVE_DISTINCE)