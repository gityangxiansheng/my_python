from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.gotosss()
    #回到起点
    def goto_POSITION(self):
        if self.ycor() >= 255:
            self.goto(STARTING_POSITION)
    
    def gotosss(self):
        self.goto(STARTING_POSITION)
    
    
    #前进MOVE_DISTANCE=10
    def forward_MOVE_DISTANCE(self):
        self.forward(MOVE_DISTANCE)
    
    


