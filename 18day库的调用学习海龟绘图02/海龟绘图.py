from turtle import Turtle,Screen

#定义timi代表海龟绘图
timi=Turtle()
#打印海龟绘图
print(timi)

#海龟绘图颜色为珊瑚色coral
timi.color("black")

#定义画笔的样式为乌龟turtle
timi.shape("classic")

for a in range(4):
    #定义画笔前进forward100
    timi.forward(100)

    #向右转
    timi.right(90                                                                                                             )

#定义my_screen（我的屏幕、窗口）为方法Screen（屏幕、窗口）
my_screen = Screen()

#打印窗口的canvheight属性，即画布的高度
print(my_screen.canvheight)

#调用exitonclick方法。这个方法的作用是设置当用户点击窗口时，程序会退出。
my_screen.exitonclick()