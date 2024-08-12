from turtle import Turtle

MOVE_DISTINCE = 50
UP = 90

class User(Turtle):
    def __init__(self,gotos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.penup()
        self.goto(gotos)
        self.setheading(UP)
    
    def up(self):
        if self.ycor() <= 200 and self.ycor() >= -250 :
            self.forward(MOVE_DISTINCE)
            
    def down(self):
        if self.ycor() <= 250 and self.ycor() >= -200 :
            self.backward(MOVE_DISTINCE)

