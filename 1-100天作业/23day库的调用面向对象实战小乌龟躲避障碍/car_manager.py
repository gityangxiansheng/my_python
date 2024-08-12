from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars =[]
        self.move=MOVE_INCREMENT
        self.car_ss=14
        

    def gotoss(self):
        random_int_car = random.randint(1, self.car_ss)
        if random_int_car == 1  or random_int_car == 2:
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.setheading(180)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            gost_y=(random.randint(-240,240))
            new_car.goto(330,gost_y)
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.move)
            
    def f5(self):
        for cars in self.all_cars:
            cars.hideturtle()
        self.all_cars =[]
    
    def move_speed(self):
        self.move *= 1.15
        self.car_ss -= 2
    
    
        

        

    
