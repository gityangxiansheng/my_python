import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#获取小乌龟并放到起始位置
us=Player()
us.goto_POSITION()
car = CarManager()
scc = Scoreboard()

screen.listen() 
screen.onkey(us.forward_MOVE_DISTANCE,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.07)
    screen.update()
    car.gotoss()
    car.move_cars()
    for cars in car.all_cars:
        if cars.distance(us) <= 20 :
            scc.over()
            game_is_on = False
            
        elif us.ycor()>255:
            us.gotosss()
            car.move_speed()
            scc.scores_promotion()


screen.exitonclick()          

        
        
    

