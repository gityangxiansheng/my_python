from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backward():
    tim.backward(10)
    
def move_backward():
    tim.backward(10)

def rotate_left():
    current_heading=tim.heading()
    tim.setheading(current_heading+10)

def rotate_right():
    current_heading=tim.heading()
    tim.setheading(current_heading-10)

def erase():
    tim.penup()
    tim.speed(0)
    tim.home()
    tim.clear()
    tim.pendown()

screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=rotate_left)
screen.onkey(key="d",fun=rotate_right)
screen.onkey(key="c",fun=erase)
screen.exitonclick()