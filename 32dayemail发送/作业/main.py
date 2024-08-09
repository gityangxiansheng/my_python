##################### Extra Hard Starting Project ######################
import pandas as pd
import random 
import smtplib 
import datetime as dt
from email.mime.text import MIMEText
from email.header import Header



def to_email(body,subject,data_email):
    #配置通信协议、构建邮件
    msg = MIMEText(body,"plain","utf-8")
    msg["Subject"] = Header(subject,"utf-8")
    msg["From"] = ""
    msg["To"] = data_email
    msg["Smtp"] = "smtp.qq.com"
    msg["password"] = ''
    smtp_port = 587

    with smtplib.SMTP(msg["Smtp"],smtp_port) as server:
        server.starttls()
        server.login(msg["From"],msg["password"])
        server.sendmail(msg["From"],msg["To"],msg.as_string())
        print("发送成功")
        
        
# 1. Update the birthdays.csv
#更新获取生日数据
data = pd.read_csv(r"python\32day\作业\birthdays.csv")
datas = [data.iloc[_].to_list() for _ in range(data.shape[0])]
print(datas)




# 2. Check if today matches a birthday in the birthdays.csv
#检查生日是否是今天
now= dt.datetime.now()
now_day = [now.year,now.month,now.day]
for data in datas:
    if data[-2:] == now_day[-2:]:
        data_name = data[0]
        data_email = data[1]
        data_year = data[2]    
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
#如是，从信件模板提取信件更改名字
        leter_list = [r"python\32day\作业\letter_templates\letter_1.txt",r"python\32day\作业\letter_templates\letter_2.txt",r"python\32day\作业\letter_templates\letter_3.txt"]

        with open(random.choice(leter_list),"r",encoding="utf-8") as leter_data:
            data_let = leter_data.read().replace("[NAME]",data_name)   
# 4. Send the letter generated in step 3 to that person's email address.
#将信件发送至电子邮件
#定义标题
        subject = f"亲爱的{data_name}! 生日快乐！！"
        body = data_let
        to_email(body,subject,data_email)





