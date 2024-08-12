# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import * 
from tkinter import messagebox
import json

# ---------------------------- SAVE PASSWORD ------------------------------- #
FONT_NAME = "Courier"
# ---------------------------- UI SETUP ------------------------------- #

    
def add_password():
    #检查字符串长度
    input_a_str=input_a.get()
    email_str=email.get()
    input_c_str=input_c.get()
    
    if len(input_a_str) == 0 or len(input_c_str) == 0:
        hint = messagebox.showerror(title="错误提示",message="请将必填项填写完毕！")
    
    else:
        confirmation_prompt = messagebox.askokcancel(title="提示",message=f"请核对您输入的信息!\n使用的应用:{input_a_str}\n账户或者邮箱:{email_str}\n密码:{input_c_str}")
        if confirmation_prompt:
            #读取json文件并储存到变量
            data_int={input_a_str:{"邮箱":email_str,"密码":input_c_str}}
            
            try:
                with open(r"C:\py4\BaiduSyncdisk\python\29day\logo.json","r",) as data_r:
                    data_r_d = json.load(data_r)
            except json.decoder.JSONDecodeError :
                with open(r"C:\py4\BaiduSyncdisk\python\29day\logo.json","w",) as data_r:
                    print("新建文件夹！")
                    json.dump(data_int,data_r,indent=4)
            except  FileNotFoundError:
                with open(r"C:\py4\BaiduSyncdisk\python\29day\logo.json","w",) as data_r:
                    print("新建文件夹！")
                    json.dump(data_int,data_r,indent=4)
            else:
                data_r_d.update(data_int)

                with open(r"C:\py4\BaiduSyncdisk\python\29day\logo.json","w",) as data_r:
                    json.dump(data_r_d,data_r,indent=4)

            finally:
                
                input_a.delete(0,END) 
                input_c.delete(0,END)
            
            messagebox.showinfo(title="保存提示",message="保存成功")
            
            #获取用户数据编写为列表 

   
        
    


window = Tk()
window.title("密码管理器")
window.config(padx=50,pady=20)

canvas_logo = Canvas(width=200,height=200)
logo_img = PhotoImage(file=r"C:\py4\BaiduSyncdisk\python\29day\logo.png")
canvas_logo.create_image(100,100,image=logo_img)
canvas_logo.grid(column=1 ,row= 0)
#标签
my_label_a = Label(text="网址：",font=(FONT_NAME,10,"bold"))
my_label_a.grid(column=0 ,row= 1)


my_label_b = Label(text="用户名/邮箱：",font=(FONT_NAME,10,"bold"))
my_label_b.grid(column=0 ,row= 2)

my_label_c = Label(text="密码：",font=(FONT_NAME,10,"bold"))
my_label_c.grid(column=0 ,row= 3)

#输入框
input_a = Entry(width=24)
input_a.focus()
input_a.grid(column=1 ,row= 1)  

email = Entry(width=35)
email.grid(column=1 ,row= 2,columnspan=2)  
email.insert(0,"1264643521@qq.com")

input_c = Entry(width=24)
input_c.grid(column=1 ,row= 3)  

def so_input_a():
    input_a_str=input_a.get()

    try:
        with open(r"C:\py4\BaiduSyncdisk\python\29day\logo.json","r",) as data_r:
            data_r_d = json.load(data_r)
            
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="提取失败",message="表格为空！请存储数据！")
    except FileNotFoundError:
        messagebox.showinfo(title="提取失败",message="未找到表格！请存储数据！")
    # except KeyError :
    #     messagebox.showinfo(title="提取失败",message=f"未找到“{input_a_str}”的密码！")
    else:
        if input_a_str in data_r_d:
            password = data_r_d[input_a_str]["密码"]
            password_l = data_r_d[input_a_str]["邮箱"]
            messagebox.showinfo(title="提取成功",message=f"应用:\n{input_a_str}\n\n邮箱：\n{password_l}\n\n密码:\n{password}")
        else:
            messagebox.showinfo(title="提取失败",message=f"未找到“{input_a_str}”的密码！")


#按钮
button_c = Button( text="生成密码",width=9)
button_c.grid(column=2 ,row= 3)
button_d = Button( text="添加记录",width=36,command=add_password)
button_d.grid(column=1 ,row= 4,columnspan=2)
button_e = Button( text="搜索一下",width=9,command=so_input_a)
button_e.grid(column=2 ,row= 1)





window.mainloop()