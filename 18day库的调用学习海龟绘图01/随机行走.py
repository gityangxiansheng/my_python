from turtle import Turtle,Screen,colormode
from random import choice,randint

def rgb():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    rgb=r,g,b
    return  rgb


def Random_Direction(color):
    colormode(255)
    aspect=[1,2,3,4]
    tim.pensize(6)
    tim.speed(0)
    for ss in range(2000):
        a=rgb()
        r=a[0]
        g=a[1]
        b=a[2]
        tim.color(r, g, b)
        aspects=choice(aspect)
        aspectss=90*aspects
        tim.right(aspectss)
        tim.forward(25)
        
    



tim = Turtle()

print(tim)
color=["red","green","blue","yellow","purple","orange","pink","black"]

Random_Direction(color)







my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()