from main import rgbss
from random import choice
import turtle as t

def paint():
    
    for s in range(10):
        random_colore = choice(rgbss)
        tim.color(random_colore)
        tim.pendown()
        tim.forward(1)
        tim.penup()
        tim.forward(50)
    tim.penup()
    tim.backward(50*10+10)
    tim.setheading(current_heading+90)
    tim.penup()
    tim.forward(50)
    tim.setheading(current_heading)


tim = t.Turtle()
print(tim)
tim.pensize(4)
tim.speed(0)
t.colormode(255)





#胎起画笔从画面中心向右上方45度前进4百码。
tim.penup()
current_heading=tim.heading()
tim.setheading(current_heading-135)
tim.forward(300)


tim.setheading(current_heading)
tim.pensize(20)



for s in range(10):
    paint()

# for s in range(10):
#     tim.pendown()
#     tim.forward(1)
#     tim.penup()
#     tim.forward(39)
#     print(current_heading)

# tim.setheading(current_heading+90)
# tim.forward(40)

# tim.setheading(current_heading+180)
# tim.penup()
# tim.forward(40)
# tim.pendown()
# tim.forward(1)
# tim.setheading(current_heading+90)

# for s in range(10):
#     tim.pendown()
#     tim.forward(1)
#     tim.penup()
#     tim.forward(39)
    
    
    
    
    

    
# for s in range(numbers):
#     tim.color(rgbss[a])
#     a += 1
    
    
    
    
#     print(tim.heading())
#     current_heading=tim.heading()
#     tim.setheading(current_heading+10)












my_screen = t.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

