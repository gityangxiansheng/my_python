from turtle import Turtle,Screen
import random 
# class Turtless():
#     def __init__(self,coler,xy):
#         self.coler=coler
#         self.xy=xy

screen = Screen()
screen.setup(width=1920,height=500)

# Turtless

def fname():

    is_race_on = True 
    y=[200,100,0,-100,-200]
    color=["red","black","blue","green","purple"]
    list_tim=[]
    for turtle_index in range(0,5):
        
        new_tim = Turtle(shape="turtle")
        new_tim.color(color[turtle_index])
        new_tim.penup()
        new_tim.speed(0)
        new_tim.goto(x=-920,y=y[turtle_index])
        list_tim.append(new_tim)
        
        
    user_input = screen.textinput(title="请选择你的小龟龟！" ,prompt="你认为什么颜色的小乌龟会赢得比赛呢?")
    print(user_input)

    if user_input:
        is_race_on = True
        
    while is_race_on:
        for s in list_tim:
            rand_distance = random.randint(0,100)
            s.forward(rand_distance)
            # colors=s.color()
            # print(colors)
            if s.xcor() >= 920:
                is_race_on = False
                if is_race_on==False:
                    colors=s.color()[0]
                    if colors == user_input:
                       sss = (f"恭喜你答对了{user_input}小乌龟胜利了！!")
                    else:
                       sss = print(f"对不起你的{user_input}小乌龟失败了!{colors}小乌龟获胜！")
                       return sss
is_race_on = True 
while is_race_on :
    fname()
    answer = screen.textinput("是否继续？", "请选择 yes 或 no：")


screen.exitonclick()