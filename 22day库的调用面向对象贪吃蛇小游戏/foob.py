from turtle import Turtle 
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()  
        self.shape("circle")
        self.speed(0)
        self.penup()
        self.color("red")
        self.shapesize(0.5,0.5)
        self.distance()
        
        
    def distance(self):
        random_x=randint(-260,260)
        random_y=randint(-260,260)
        self.goto(random_x,random_y)
        