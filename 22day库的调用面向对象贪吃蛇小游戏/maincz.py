from turtle import Turtle,Screen
import time

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("贪 吃 蛇 ")

screen.tracer(n=0)

xx=[(0,0),(-20,0),(-40,0)]
tim_list=[]
for a in xx:
    tim =Turtle()
    tim.color("white")
    tim.shape("square")
    tim.penup()
    tim.goto(a)
    tim_list.append(tim)


genme_is_on = True
while genme_is_on:
    screen.update()
    time.sleep(0.2)
    for tim_num in range(len(tim_list)-1,0,-1):
        new_x=tim_list[tim_num-1].xcor()
        new_y=tim_list[tim_num-1].ycor()
        tim_list[tim_num].goto(new_x,new_y)
        
    tim_list[0].forward(20)
        
        
        
        
        

screen.exitonclick()