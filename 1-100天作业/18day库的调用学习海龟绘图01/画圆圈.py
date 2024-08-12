import turtle as t
from random import randint

def rgb():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    
    return  r,g,b

def number(numbers):
    a=1100/numbers
    return a

tim = t.Turtle()

print(tim)
tim.pensize(3)
tim.speed(0)
t.colormode(255)

numbers=1200
circles=180

for s in range(numbers):
    rgbs=rgb()
    tim.color(rgbs[0],rgbs[1],rgbs[2])
    tim.circle(circles)
    print(tim.heading())
    current_heading=tim.heading()
    tim.setheading(current_heading+number(numbers))




my_screen = t.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
