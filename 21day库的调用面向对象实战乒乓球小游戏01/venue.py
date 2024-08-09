from turtle import Turtle,Screen

class Venue(Turtle):
    """创建一个黑色的画布 然后中间有一条虚线"""
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.color("white")
        self.goto(0,290)
        #角度270度
        self.seth(270)
        #画笔大小六个像素
        self.pensize(6)
        #隐藏笔触
        self.hideturtle()
        #画出虚线
        self.fnvenue_size_screen()
        
        # self.angle = self.heading()
    
    def line(self):
        """画虚线的方法"""
        
        self.pendown()
        self.fd(30)
        self.penup()
        self.fd(30)
        
    def fnvenue_size_screen(self):
        """画虚线从上到下"""
        while self.ycor() >= -300:
            self.line()

        
            


 