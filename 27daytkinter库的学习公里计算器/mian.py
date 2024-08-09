from tkinter import *

window = Tk()
window.title("我的框框")
window.minsize(width=600,height=600)

my_label = Label(text="我的显示文字",font=("Arial",24))
my_label.pack()

# my_label["text"] = "New Text"
# my_label.config(text="New Text")

def button_clicked():
    ss=input.get()
    my_label["text"] = ss
    
    


input = Entry(width=10)
input.pack()     




button = Button( text="我的按钮",command=button_clicked)
button.pack()





window.mainloop()

# my_label = label( )