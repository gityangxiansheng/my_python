import turtle
import pandas as pd

data=pd.read_csv(r"C:\py4\BaiduSyncdisk\python\25day\50_states.csv")
image = r"C:\py4\BaiduSyncdisk\python\25day\blank_states_img.gif"

screen = turtle.Screen()
screen.title("u.s")
screen.addshape(image)
turtle.shape(image)

all_states=data["state"].to_list()
huessed_states = []

#如果正确输入的的地方列表未超过小于50，开始循环。
while len(huessed_states) < 50 :
    #输入城市answer_state
    answer_state = screen.textinput(title=f"{len(huessed_states)}/50",prompt="您要选择的城市是？").lower().title()
    #判断输入是否等于退出，如果等于退出
    if answer_state == "Exit":
        #建立一个新列表
        missin_states = [ state for state in all_states if state not in huessed_states]
        #循环文件中的每个地方的名字
        #如果文件中每个地方的名字都不存在于已输入的列表中
        #存储总文件中的地方名到新列表中
        # for state in all_states:
        #     if state not in huessed_states:
        #         missin_states.append(state)

        #创建一个新的数据框架
        new_data = pd.DataFrame(missin_states)
        #储存为csv
        new_data.to_csv(r"C:\py4\BaiduSyncdisk\python\25day\datas.csv")

    #如果输入的地方名存在于文件的文件名列表中
    if answer_state in all_states:
        #输入列表获取当前输入内容
        huessed_states.append(answer_state)
    #利用turtle库在指定位置画出指定的输入地方名
        #获取库
        t = turtle.Turtle()
        #隐藏画笔、乌龟
        t.hideturtle()
        #抬起画笔
        t.penup()
        #获取指定行（输入数据）的数据框架
        state_data = data[data.state  == answer_state]
        #画笔前往数据框架内x和y列的位置
        t.goto(int(state_data.x), int(state_data.y))
        #画笔画出（输入的地方名）
        t.write(answer_state)
