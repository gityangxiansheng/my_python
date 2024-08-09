from tkinter import *

window = Tk()
window.title("这是一个公里转换器")
# window.minsize(width=300,height=160)
window.config(padx=30,pady=30)

my_label_a = Label(text="里地",font=("Arial",16))
my_label_a.grid(column=3 ,row= 1)

my_label_b = Label(text="公里",font=("Arial",16))
my_label_b.grid(column=3 ,row= 2)

my_label_c = Label(text="等于",font=("Arial",16))
my_label_c.grid(column=1 ,row= 2)

my_label_d = Label(text="0",font=("Arial",16))
my_label_d.grid(column=2 ,row= 2)

# my_label["text"] = "New Text"
# my_label.config(text="New Text")

def button_clicked():
    ss=input.get()
    my_label_d["text"] = int(int(ss)/2)
    
    


input = Entry(width=10)
input.grid(column=2 ,row= 1)   




button = Button( text="我的按钮",command=button_clicked)
button.grid(column=2 ,row= 3)





window.mainloop()

# my_label = label( )