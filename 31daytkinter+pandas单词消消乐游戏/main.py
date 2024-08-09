from tkinter import *
import csv
import pandas
import random
#==========================data===========================
#色号
BACKGROUND_COLOR = "#B1DDC6"
#四个图片位置
card_back=r"C:\Users\Administrator\Desktop\BaiduSyncdisk\python\31day\images\card_back.png"
card_front=r"C:\Users\Administrator\Desktop\BaiduSyncdisk\python\31day\images\card_front.png"
right=r"C:\Users\Administrator\Desktop\BaiduSyncdisk\python\31day\images\right.png"
wrong=r"C:\Users\Administrator\Desktop\BaiduSyncdisk\python\31day\images\wrong.png"
#数据位置
data_frenchi=r"C:\Users\Administrator\Desktop\BaiduSyncdisk\python\31day\data\french_words.csv"
new_data=r"C:\Users\Administrator\Desktop\BaiduSyncdisk\python\31day\data\new_french_words.csv"
#==========================DEF===========================
# pandas方法
try:
    data = pandas.read_csv(new_data)
except FileNotFoundError:
    data = pandas.read_csv(data_frenchi) 


datar = data.to_dict(orient="records")
# print(datar)
current_card={}
#下一个卡片        
def yes_on ():
    global current_card,after_time
    
    window.after_cancel(after_time)
    if len(datar)>1:
        current_card=random.choice(datar)
        card.itemconfig(book,image=card_img)
        card.itemconfig(language_type,text="French",fill="black")
        card.itemconfig(word,text=current_card["French"],fill="black")
        after_time = window.after(3000,func=flip_card)
    else: 
        print("学成了！！！")
        card.itemconfig(book,image=card_img)
        card.itemconfig(language_type,text="恭喜你",fill="black")
        card.itemconfig(word,text="游戏结束！",fill="black")

    # print(current_card)
    # card.itemconfig(book,image=card_img)
    # card.itemconfig(language_type,text="French",fill="black")
    # card.itemconfig(word,text=current_card["French"],fill="black")
    # after_time = window.after(3000,func=flip_card)
#正确后储存新的csv
def yes_on_move():
    global datar
    datar.remove(current_card)
    print(len(datar))
    datas=pandas.DataFrame(datar)
    datas.to_csv(new_data,index=False)
    print(datas)
    yes_on()
    
    
#三秒后卡片反转
def flip_card():
    global current_card
    card.itemconfig(book,image=card_img_back)
    card.itemconfig(language_type,text="English",fill="white")
    card.itemconfig(word,text=current_card["English"],fill="white")
     
        
    
        



#==========================UI===========================
#窗口
window = Tk()
window.title("单词消消乐")
window.config(padx=100,pady=100,bg=BACKGROUND_COLOR)

after_time=window.after(3000,func=flip_card)

#画布
card = Canvas(width=800,height=526)
card_img = PhotoImage(file=card_front)
card_img_back = PhotoImage(file=card_back)
book=card.create_image(400,263,image=card_img)
card.config(bg=BACKGROUND_COLOR,highlightthickness=0)
language_type = card.create_text(400,150,text="English",font=("Ariel",40,"italic"))
word = card.create_text(400,260,text="word",font=("Ariel",60,"bold"))
card.grid(column=1,row=0,columnspan=2)

#按钮
card_img_yes=PhotoImage(file=right)
card_img_no=PhotoImage(file=wrong)

button_yes = Button(image=card_img_yes,command=yes_on_move)
button_yes.grid(column=2 ,row= 1)

button_no = Button(image=card_img_no,command=yes_on)
button_no.grid(column=1 ,row= 1)





yes_on()






window.mainloop()







#==========================DEF===========================


