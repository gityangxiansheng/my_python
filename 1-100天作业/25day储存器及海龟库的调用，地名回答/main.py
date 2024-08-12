import turtle
import pandas as pd

csv_data=pd.read_csv(r"C:\py4\BaiduSyncdisk\python\25day\50_states.csv")
image = r"C:\py4\BaiduSyncdisk\python\25day\blank_states_img.gif"

tim=turtle
screen = tim.Screen()
screen.title("u.s")
screen.addshape(image)
tim.shape(image)

us = True
input_us = []
ss_state_rusd=csv_data["state"].to_list()
while us:
    if len(input_us) < 50 :
        int_us = screen.textinput(title=f"{len(input_us)}/50",prompt="您要选择的城市是？").lower().title()
        ss_list = csv_data[csv_data.state==int_us]
        ss_x=ss_list["x"].to_list()
        ss_y=ss_list["y"].to_list()
        ss_state=ss_list["state"].to_list()

        if int_us == "Exit":
            break
        elif ss_list.empty :
            print("答错了")
        else:
            if not ss_state[0] in input_us:
                print("答对了")
                print(ss_state[0])
                ss_state_rusd.remove(ss_state[0])
                print(ss_state_rusd)
                ss_state_dict = {"未答对":ss_state_rusd}
                # print(ss_state_dict)
                pen_tim = turtle.Turtle()
                pen_tim.penup()
                pen_tim.hideturtle()
                pen_tim.goto(ss_x[0],ss_y[0])
                pen_tim.write(f"{ss_state[0]}",align="center",font=("Arial",8,"normal"))
                input_us.append(ss_state[0])
                datas = pd.DataFrame(ss_state_dict)
                # print(datas)
                datas.to_csv(r"C:\py4\BaiduSyncdisk\python\25day\datas.csv")
                # ss_state.remove(input_us)
                # print(input_us)
            else:
                print("啊偶！回答重复了！")


