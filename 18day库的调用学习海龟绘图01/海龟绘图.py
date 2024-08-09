from turtle import Turtle,Screen
from random import random,choice

# {insert\_element\_1\_dHVydGxl}.forward(distance)：向前移动画笔一段距离，参数distance表示移动的距离。
# turtle.right(angle)：向右旋转画笔角度，参数angle表示旋转的角度。
# turtle.left(angle)：向左旋转画笔角度。
# turtle.circle(radius, extent=None)：绘制圆形，参数radius表示圆的半径，extent（可选）表示绘制的弧度（范围是 0 到 360）。
# turtle.penup()：抬起画笔，移动时不会绘制图形。
# turtle.pendown()：放下画笔，开始绘制图形。
# turtle.goto(x, y)：将画笔移动到指定的坐标(x, y)。
# turtle.fillcolor(color)：设置填充颜色。
# turtle.begin_fill()：开始填充图形。
# turtle.end_fill()：结束填充图形。
def polygon(amount,color):
    
    angle=360/amount
    timi.color(color)
    for ss in range(amount):
        timi.right(angle)
        timi.forward(100)


#定义turtle 为timi
timi=Turtle()
#打印timi，
print(timi)

#shape方法设置画笔样式
timi.shape("arrow")

color=["red","green","blue","yellow","purple","orange","pink","white","black"]


for ss in range(3,30):
    colors=choice(color)
    polygon(ss,colors)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


