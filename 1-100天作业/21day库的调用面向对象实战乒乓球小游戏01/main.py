from turtle import Turtle ,Screen
from venue import Venue
from user import User
from ball import Ball
from scoreboard import Scoreboard

import time

screen=Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("乒 乓 球")
screen.tracer(0)

a=Venue()
b=User()
d=Ball()
ss=Scoreboard()

screen.listen()
screen.onkey(key="Up",fun=b.up)
screen.onkey(key="Down",fun=b.down)
screen.onkey(key="w",fun=b.up_2)
screen.onkey(key="s",fun=b.down_2)

genme_is_on = True
d.reft_left_create()
while genme_is_on:
    screen.update()
    time.sleep(0.01)
    d.forward(3)
    y_ycor=d.ycor()
    x_ycor=d.xcor()
    # print(y_ycor,x_ycor)
    ss.scores_1()
    if y_ycor >= 280 or y_ycor <= -280:
        d.rebound()

    elif x_ycor >= 495:
        ss.us1_scores()
        d.goto_s()
        d.reft_left_create()
        

        
        
    elif x_ycor <= -495:
        ss.us2_scores()
        d.goto_s()
        d.reft_left_create()
        
    else:
        for s in range(0,len(b.user_1)):
            if b.user_1[s].distance(d) <= 18:
                d.rebound()
            elif b.user_2[s].distance(d) <= 18:
                d.rebound()
            
    


screen.exitonclick()