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

gosot=(460,0)
gosots=(-470,0)
scoreboard_gosot1=(-50,240)
scoreboard_gosot2=(50,240)
a=Venue()
users1=User(gosot)
users2=User(gosots)
d=Ball()


    
screen.listen()

screen.onkey(key="Up",fun=users1.up)
screen.onkey(key="Down",fun=users1.down)


screen.onkey(key="w",fun=users2.up)
screen.onkey(key="s",fun=users2.down)






genme_is_on = True
users_sc=Scoreboard()
users_sc.prints()
# users2_sc=Scoreboard(scoreboard_gosot2,得分)
while genme_is_on:
    screen.update()
    time.sleep(d.move_speed)
    d.move()

    # print(y_ycor,x_ycor)
    # ss.scores_1()
    
    if d.ycor() >= 280 or d.ycor() <= -280:
        d.bounce_y()
   
    if d.distance(users1) <= 50 and d.xcor() > 440 or d.distance(users2) <= 50 and d.xcor() < -440:
        d.bounce_x() 

    elif d.xcor() >= 495:
        users_sc.l_scoress()
        d.goto_s()

    elif d.xcor() <= -495:
        users_sc.r_scoress()
        d.goto_s()

            
    


screen.exitonclick()