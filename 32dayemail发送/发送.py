import smtplib 
from email.mime.text import MIMEText
from email.header import Header
import datetime as dt
import random 



with open(r"python\32day\quotes.txt","r",encoding="utf-8")as txtt:
    rtxt = txtt.readlines()
    dy_tst = random.choice(rtxt)
    


now = dt.datetime.now()
nows = [now.year,now.month,now.day]
my_time = [2023,3,29]
print(nows)

print(my_time)


# if my_time == nows:
#     #邮件内容
#     #标题
#     subject = "每日正念"
#     body = dy_tst
#     from_email = ""
#     to_email = ""

#     #构建邮件
#     #邮件的本体格式、邮件的标题格式、邮件来自、邮件去往
#     msg = MIMEText(body,"plain","utf-8")
#     msg['Subject'] = Header(subject,"utf-8")
#     msg["From"] = from_email
#     msg["To"] = to_email

#     #发送邮件
#     smtp_server = "smtp.qq.com"
#     smtp_port = 587
#     sender_email = 
#     password = 


#     # 调用服务器发送邮件并关闭链接
#     # 传入服务器及端口号
#     with smtplib.SMTP(smtp_server,smtp_port) as server:
#         #开启数据加密
#         server.starttls()
#         #传入用户名密码
#         server.login(sender_email,password)
#         #发送邮件！
#         # 传入发件人地址、
#         # 收件人地址（可以是单个地址、也可以是一个地址列表）、
#         # 邮件内容
#         server.sendmail(from_email,to_email,msg.as_string())
#         print("已发送")
# else:
#     print(f"距离发送时间还有：{my_tim_year-now_year}年，{my_tim_mont-now_mont}月，{my_tim_day-now_day}日")



