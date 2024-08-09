from main import rgbss
from random import choice
import turtle as t

def paint():
    for s in range(10):
        random_colore = choice(rgbss)
        tim.color(random_colore)        
        tim.dot(20,random_colore)
        tim.forward(50)
    tim.backward(50*10)
    tim.setheading(current_heading+90)
    tim.forward(50)
    tim.setheading(current_heading)


tim = t.Turtle()
print(tim)
tim.pensize(4)
tim.speed(0)
t.colormode(255)





#胎起画笔从画面中心向右上方45度前进4百码。
tim.penup()
tim.hideturtle()
current_heading=tim.heading()
tim.setheading(current_heading-135)
tim.forward(300)

tim.setheading(current_heading)




for s in range(10):
    
    paint()


    
    
my_screen = t.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

