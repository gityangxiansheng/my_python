from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
wrong=r"python\34day\images\false.png"
right=r"python\34day\images\true.png"

class QuizIntenrface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        #窗口设置
        self.window = Tk()
        self.window.title("更高更高")
        self.window.config(padx=0,pady=20,bg=THEME_COLOR)
        self.label = Label(text=f'得分：00', font=('Arial', 16),fg="white")
        self.label.config(bg=THEME_COLOR)
        self.label.grid(column=2,row=0)
        #画布设置
        self.canvas = Canvas(width=300,height=300)
        self.canvas.config(bg="white")
        self.language = self.canvas.create_text(150,150,text="English",font=("Ariel",20,"italic"),
                                                width=280
                                                )
        self.canvas.grid(column= 1 ,row= 1,columnspan=2,padx=30, pady=40)
        #按钮设置
        self.card_img_yes=PhotoImage(file=right)
        self.card_img_no=PhotoImage(file=wrong)
        self.button_yes = Button(image=self.card_img_yes,highlightthickness=0,command=self.inpt_yes)
        self.button_yes.grid(column=1,row=3)
        self.button_no = Button(image=self.card_img_no,highlightthickness=0,command=self.inpt_on)
        self.button_no.grid(column=2,row=3)
        self.up_language()
        self.window.mainloop()
        # up_language(self)
        # #更新得分
        # self.window.mainloop()
        
    def up_language(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f'得分：{self.quiz.score}')
            txt = self.quiz.next_question()
            self.canvas.itemconfig(self.language,text=txt)
        else :
            self.canvas.itemconfig(self.language,text="你已经答完全部题目!!")
            self.button_no.config(state="disabled")
            self.button_yes.config(state="disabled")
    def inpt_yes(self):
        self.ye_on(self.quiz.check_answer("True"))
        
    def inpt_on(self):
        is_right = self.quiz.check_answer("False")
        self.ye_on(is_right)
    
    def ye_on(self,is_right):
        
        if is_right:
            print("答对")
            self.canvas.config(bg="green")
        else:
            print("cuole")
            self.canvas.config(bg="red")
        self.window.after(1000,self.up_language)

            
            
        
        

            
        
            
        # self.window.mainloop()
        
        


 

            


        


