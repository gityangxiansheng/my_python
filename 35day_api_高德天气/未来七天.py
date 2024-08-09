import requests
import json
import pandas as pd
import random 
import smtplib 
import datetime as dt
from email.mime.text import MIMEText
from email.header import Header

######################################邮件
def to_email(body, subject, data_email):  
    # 从环境变量或配置文件中获取敏感信息  
    email_password = ''
    sender_email = "@163.com"  
    smtp_server = "smtp.163.com"  
    smtp_port = 465  
  
    # 配置通信协议、构建邮件  
    msg = MIMEText(body, "plain", "utf-8")  
    msg["Subject"] = Header(subject, "utf-8")  
    msg["From"] = sender_email  
    msg["To"] = data_email  
  
    # 使用ssl模块的context加载系统允许的证书，在登录时进行验证  
    
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:  
        try:  
            server.login(sender_email, email_password)  
            server.sendmail(sender_email, data_email, msg.as_string())  
        except smtplib.SMTPException as e:  
            print(f"Error: unable to send email - {e}") 



####################################################天气
ss = {
    "lat":34.83961588746689,
    "lon":113.93433316635135,
    "appid":"654e80f17426bdc87e9b65bb1286557c",
    "lang":"zh_cn",
    "units":"metric",
    # "cnt":7
}
ulr="https://api.openweathermap.org/data/2.5/forecast"



#转表格
data = requests.get(ulr,params=ss)
datas = data.json()
data_df={}
for _ in range(len(datas["list"])):
    data_df[_]=[
        datas["list"][_]["dt_txt"],
        datas["list"][_]["main"]["feels_like"],
        datas["list"][_]["main"]["temp_max"],
        datas["list"][_]["main"]["temp_min"],
        datas["list"][_]["weather"][0]["description"],
        datas["list"][_]["wind"]["speed"],
       datas["list"][_]["weather"][0]["id"]
        ]

#转表格
df = pd.DataFrame(data_df).T
df.columns = ['日期', '体感温度',"最高温度","最低温度","天气","风速","气候ID"]
df.to_excel(r"C:\Users\Administrator\Desktop\BaiduSyncdisk\python\35day_api_高德天气\ssc.xlsx", sheet_name='Sheet1', index=False)
ts = []

for index,id_d in enumerate(df['气候ID'][0:4]):
    if id_d < 600:
        ts.append("雨")
    if int(df["风速"][index]) >= 6:
        ts.append("风")
    if id_d > 600 and id_d < 700:
        ts.append("雪")
if "风" in ts and "雨" in ts and "雪" in ts:
    subject="未来十二小时有风有雨且有雪，尽量呆在家里吧！"
elif "风" in ts and "雪" in ts :
    subject="大风夹雪，打脸生疼,外出带个面具吧！"
elif "雨" in ts and "雪" in ts:
    subject="大风加雨，外出小心！"
elif "风" in ts:
    subject="小心大风，外出觅食要小心！"
elif "雨" in ts :
    subject="小心有雨，外出觅食要带伞！"
elif "雪" in ts :
    subject="小心积雪，外出觅食注意防滑！"
else:
    subject="天气还不错！出门逛逛吧！"


############################################################身体
datt = pd.read_excel(r"C:\Users\Administrator\Desktop\BaiduSyncdisk\python\35day_api_高德天气\zhaichao.xls")
dat_list = datt.values.tolist()
body=(f"最高温度:{max(df["最高温度"][0:4])},最低温度:{min(df["最低温度"][0:4])}\n\n\n"
      f"《每日一学》\n\n\n"
    f"\t{random.choice(dat_list)[0]}\n\n\n"
    f"\t{random.choice(dat_list)[0]}\n\n\n"
    f"\t{random.choice(dat_list)[0]}\n\n\n"
    )
with open(r"C:\Users\Administrator\Desktop\BaiduSyncdisk\python\35day_api_高德天气\dssds.txt","r") as dssttx:
    gmails=dssttx.readlines()
    gmai_list=gmails[0].split(",")
    
for _ in gmai_list:
    to_email(body,subject,_)