from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer_s=None

    

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

#定义一个停止函数，停止计数并且归0 ，去掉所有标记，将状态更改为番茄时钟
def stop_timer():
    window.after_cancel(timer_s)
    canvas.itemconfig(timer_text,text=f'00:00')
    my_label_a.config(text="Timer",fg=GREEN)
    emoj = ""
    my_label_b.config(text=emoj) 
    global REPS
    REPS = 0


#定义一个时间计算函数，分别将常量的分钟数转化为秒数，并设置循环25-5，25-5，25-5，25-20
#定义启动函数！用以按钮操控
def start_timer():
    global REPS
    REPS += 1
    print(REPS)
    work_esc = WORK_MIN * 60 
    short_break_esc = SHORT_BREAK_MIN * 60
    long_break_esc = LONG_BREAK_MIN * 60
    
    if REPS == 1 or REPS == 3 or REPS == 5 or REPS == 7:
        say_sonmething(work_esc)
        my_label_a.config(text="努力工作",fg=GREEN)
        
        
    if REPS == 2 or REPS == 4 or REPS == 6:
        say_sonmething(short_break_esc)
        print("休息5分钟")
        my_label_a.config(text="正在休息",fg=RED)
    if REPS == 8 :
        say_sonmething(long_break_esc)
        my_label_a.config(text="正在休息",fg=PINK)
        print("休息20分钟")
        REPS = 0

#定义一个时间显示函数，分数等于秒数除以60，剩余总秒数除以60剩余的数为应该显示的秒数，时间显示规则为：小于0的整数显示00.
def say_sonmething(timess_minutes):
    #总秒数除以60
    timess_minutess=int(timess_minutes / 60)
    #如果总秒数大于0就每秒总秒数-1
    if timess_minutes > 0:
        global timer_s
        timer_s = window.after(5,say_sonmething,timess_minutes-1)
    #时间显示规则为：小于0的整数显示00.
    if timess_minutess < 10 :
        timess_minutess = f"0{timess_minutess}"
    #总秒数除以60取模    
    timess_minutesss=int(timess_minutes % 60)
    #时间显示规则为：小于0的整数显示00.
    if timess_minutesss < 10:
        timess_minutesss = f"0{timess_minutesss}"
    if timess_minutes == 0:
        print(f"{timess_minutes}")
        start_timer()
        emoj = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            emoj += "✌️"
        my_label_b.config(text=emoj)
    #将时间显示到画布上以*：*的形式
    print(f"{timess_minutes}")
    canvas.itemconfig(timer_text,text=f'{timess_minutess}:{timess_minutesss}')
    
    
        

# ---------------------------- UI SETUP ------------------------------- #
#建立窗口
window = Tk()
window.title("番茄工作法")
window.config(padx=100,pady=50,bg=YELLOW)


#设置画布大小，导入番茄图片，画布上添加一组文字倒计时。
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file=r"BaiduSyncdisk/python/28day/tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold")) 
#定义画布在窗口中的位置第二列-第二行
canvas.grid(column=2 ,row= 2)

#设置文字并定义文字位置。
my_label_a = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,36,"bold"))
my_label_a.grid(column=2 ,row= 1)
#设置文字并定义文字位置。
my_label_b = Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,10,"bold"))
my_label_b.grid(column=2 ,row= 4)
#设置按钮并定义按钮位置。
button = Button( text="开始",command=start_timer)
button.grid(column=1 ,row= 3)
#设置按钮并定义按钮位置。
button = Button( text="我的按钮",command=stop_timer)
button.grid(column=3 ,row= 3)








window.mainloop()