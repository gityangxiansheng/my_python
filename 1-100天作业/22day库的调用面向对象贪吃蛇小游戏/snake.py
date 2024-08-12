from turtle import Turtle , Screen
import time
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTINCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """蛇"""
    def __init__(self):
        self.tim_list=[]
        self.create_snake()
        self.head=self.tim_list[0]
    
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)                 


    def add_segment(self,position):
        tim =Turtle()
        tim.color("white")
        tim.shape("square")
        tim.penup()
        tim.goto(position)
        self.tim_list.append(tim) 


    def snake_close(self):
        for tims in self.tim_list:
            tims.goto(1000,1000)
        self.tim_list.clear()
        self.create_snake()
        self.head=self.tim_list[0]
        
    
    def exetend(self):
        self.add_segment(self.tim_list[-1].position())



    def move(self):
        for tim_num in range(len(self.tim_list)-1,0,-1):
            new_x=self.tim_list[tim_num-1].xcor()
            new_y=self.tim_list[tim_num-1].ycor()
            self.tim_list[tim_num].goto(new_x,new_y)
        self.tim_list[0].forward(MOVE_DISTINCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
