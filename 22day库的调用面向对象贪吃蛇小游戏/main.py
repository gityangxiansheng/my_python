from snake import Snake
from turtle import  Screen
from foob import Food
from scoreboard import Scoreboard
import time



screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("贪 吃 蛇 ")

screen.tracer(0)

snake_s=Snake()

food=Food()
scs = Scoreboard()

screen.listen()
screen.onkey(key="Up",fun=snake_s.up)
screen.onkey(key="Down",fun=snake_s.down)
screen.onkey(key="Left",fun=snake_s.left)
screen.onkey(key="Right",fun=snake_s.right)



genme_is_on = True
while genme_is_on:
    screen.update()
    time.sleep(0.2)
    snake_s.move()

    
    if snake_s.head.distance(food) < 15:
        food.distance()
        snake_s.exetend() 
        scs.scoress()
        

    if snake_s.head.xcor() > 280 or  snake_s.head.xcor() < -280 or snake_s.head.ycor() > 280 or  snake_s.head.ycor() < -280:
        
        snake_s.snake_close()
        scs.reset()
        scs.f5()
        
        
    
    for s in snake_s.tim_list[1:]:
        if snake_s.head.distance(s) < 10:

            snake_s.snake_close()
            scs.reset()
            scs.f5()
            # genme_is_on = False
        


screen.exitonclick()