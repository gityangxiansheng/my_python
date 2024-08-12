import requests
import json
import pandas as pd
from datetime import datetime, timedelta

import smtplib
from email.mime.text import MIMEText
from email.header import Header

STOCK = "TSLA"
# COMPANY_NAME = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#定义函数获取数据信息储存至json
def hqshuj():
    url = 'https://www.alphavantage.co/query'
    parameters = {
        "function":"TIME_SERIES_DAILY",
        "symbol":STOCK,
        "interval":"1min",
        "apikey":""
    }
    r = requests.get(url,parameters)
    r_data = r.json()
    with open (r"python\36day\main.json","w") as rs:
        json.dump(r_data,rs)

#获取今天的时间日期，并格式化
now_tm= datetime.now() - timedelta(days=2)
year = now_tm.year
month = str(now_tm.month).zfill(2)
day = str(now_tm.day).zfill(2)
now_days = f"{year}-{month}-{day}"

#获取昨天的时间日期，并格式化
tow_tm = now_tm - timedelta(days=1)
tow_year = tow_tm.year
tow_month = str(tow_tm.month).zfill(2)
tow_day = str(tow_tm.day).zfill(2)
tow_days = f"{tow_year}-{tow_month}-{tow_day}"

#打开json 文件查看文件内容    
with open (r"python\36day\main.json","r") as r:
    data = json.load(r)
#获取数据
name = data["Meta Data"]["2. Symbol"]
datas = data["Time Series (Daily)"]
print(datas)
#获取每日开盘价，如果开盘价和昨日开盘价相差超过百分之5：
now_data = datas[now_days]
tow_data = datas[tow_days]




try:
    
    #打开json 文件查看文件内容    
    with open (r"python\36day\main.json","r") as r:
        data = json.load(r)
#获取数据
    name = data["Meta Data"]["2. Symbol"]
    datas = data["Time Series (Daily)"]
    #获取每日开盘价，如果开盘价和昨日开盘价相差超过百分之5：
    now_data = datas[now_days]
    tow_data = datas[tow_days]
except KeyError:
    hqshuj()
    with open (r"python\36day\main.json","r") as r:
        data = json.load(r)
    #获取数据
    name = data["Meta Data"]["2. Symbol"]
    datas = data["Time Series (Daily)"]
    now_data = datas[now_days]
    tow_data = datas[tow_days]
except FileNotFoundError :
    hqshuj()
    with open (r"python\36day\main.json","r") as r:
        data = json.load(r)
    #获取数据
    name = data["Meta Data"]["2. Symbol"]
    datas = data["Time Series (Daily)"]
    now_data = datas[now_days]
    tow_data = datas[tow_days]
#昨天的百分比减去前天的百分比等于百比的差

now_open_data = float(now_data["1. open"])
tow_open_data = float(tow_data["1. open"])
print("这是昨天的数据",now_open_data)

cha = (now_open_data - tow_open_data)/now_open_data
# print("数据的差",cha)
data_s = now_open_data*0.05
# print("这是百分比",data_s)
if now_open_data - tow_open_data > data_s or tow_open_data - now_open_data > data_s :
    print("超过百分之5")
else :
    print(cha)


"1FZBH0DNXPUM07IM"
    
def ff():
    url = 'https://www.alphavantage.co/query'
    parameters = {
        "function":"NEWS_SENTIMENT",
        "tickers":STOCK,
        "apikey":""
    }
    NEWS_SENTIMENT = requests.get(url,parameters)
    ma = NEWS_SENTIMENT.json()
    with open (r"python\36day\mainss.json","w") as mainss:
        json.dump(ma,mainss)

        


with open (r"python\36day\mainss.json","r") as mainss:
    main = json.load(mainss)
# print(type(main))
# print(main["feed"][1])

tsla={} 
for ss in main["feed"]:
    # print(ss['ticker_sentiment'])
    for  s in ss['ticker_sentiment']:
        if s['ticker'] == 'TSLA'and float(s['relevance_score']) > 0.6:
            # print(ss["title"])
            # print(ss["url"])
            # print(s['relevance_score'])
            # print("\n")
            tsla[float(s['relevance_score'])] = {"title":ss["title"],"url":ss["url"]}
tslas= dict(sorted(tsla.items(),reverse=True))

cc = 0


xinwen = []
for _ in tslas:

    if cc < 3:
        xinwen.append(tslas[_])
        cc += 1 
    else :
        break
        # print(ss['ticker_sentiment'][1],"\n")
        # print("\n\n")
        # print(ss['ticker_sentiment'][0]["ticker"],"\n")

# ssd = requests.get(r"https://www.cnn.com/2024/04/03/cars/china-tesla-byd-competition-hnk-intl-dg/index.html")
# scv=ssd.text
# print(scv)
print(type(xinwen))
print(cha)
#昨天今天的差是：che 相关性排序三个新闻是xinwen
def to_email(body, subject, data_email):  
    # 从环境变量或配置文件中获取敏感信息  
    email_password = ''
    sender_email = "@163.com"  
    smtp_server = "smtp.163.com"  
    smtp_port = 465  
  
    # 配置通信协议、构建邮件  
    msg = MIMEText(body,"plain","utf-8")  
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
            
body= f"根据相关度排序新闻！\n{xinwen[0]}\n\n\n{xinwen[1]}\n\n\n{xinwen[2]}"
subject= f"特斯拉股值相较昨日{cha}"
to_email(body=body,subject=subject,data_email="@qq.com")




## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 




## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

