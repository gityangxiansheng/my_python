import requests
import json
import pandas as pd
from datetime import datetime, timedelta
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"




## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
url = 'https://www.alphavantage.co/query'
parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "interval":"1min",
    "apikey":"RMCECXTL4EJZJCW7"
}
with open (r"C:\py4\BaiduSyncdisk\python\36day\main.json","r") as r:
# r = requests.get(url,parameters)
    data = json.load(r)

name = data["Meta Data"]["2. Symbol"]
datas = data["Time Series (Daily)"]

#获取今天的时间日期，并格式化
now_tm= datetime.now() - timedelta(days=1)
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

print(datas)
#获取每日开盘价，如果开盘价和昨日开盘价相差超过百分之5：
now_data = datas[now_days]
tow_data = datas[tow_days]

now_open_data = float(now_data["1. open"])
tow_open_data = float(tow_data["1. open"])

data_s = now_open_data*0.05

if now_open_data - tow_open_data > data_s or tow_open_data - now_open_data > data_s :
    print("超过百分之5")
else :
    print(now_open_data - tow_open_data)


""
    

# url = 'https://www.alphavantage.co/query'
# parameters = {
#     "function":"",
#     "tickers":STOCK,
#     "apikey":""
# }
# NEWS_SENTIMENT = requests.get(url,parameters)

# ma = NEWS_SENTIMENT.json()
# print(ma)

with open (r"C:\py4\BaiduSyncdisk\python\36day\mainss.json","r") as mainss:
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
for _ in tslas:
    if cc < 3:
        print(tslas[_],"\n")
        cc += 1 
    else :
        break
        # print(ss['ticker_sentiment'][1],"\n")
        # print("\n\n")
        # print(ss['ticker_sentiment'][0]["ticker"],"\n")

# ssd = requests.get(r"https://www.cnn.com/2024/04/03/cars/china-tesla-byd-competition-hnk-intl-dg/index.html")
# scv=ssd.text
# print(scv)







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

