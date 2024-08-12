import requests 
from datetime import datetime  
from dateutil.relativedelta import relativedelta  

ArrCity = "HGH"

#抓取近三个月数据data为主要修改内容arrCity为ata机场代号month为月份
now = datetime.now()  
nows = now + relativedelta(months=1)  
formatted_now = nows.strftime("%m")
datav=[]
for s in range(3):
    nows = now + relativedelta(months=s) 
    formatted_now = nows.strftime("%m")
    print(formatted_now)
    url = "https://b2c.csair.com/portal/minPrice/queryMinPriceInMonth?type__1188=QqRxnDyDRDc7oGNDQiiQA8wxjx6ODBlOoD"
    headers={
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Cookie":"",
        "Referer":"https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=CGO&c2=HGH&d1=2024-04-30&at=1&ct=0&it=0&b1=CGO&b2=HGH",
        "Sec-Fetch-Site":"same-origin",
        }
    data={'dep': "", 'arr': "", 'depCity': "CGO", 'arrCity': f"{ArrCity}", 'month': f"2024-{formatted_now}", 'channel': "B2CPC1"}
    datas = requests.post(url=url,headers=headers,json=data).json()
    for ss in datas["data"]:
        datav.append(ss)

# datav = [{'date': '2024-04-15', 'price': 400}, {'date': '2024-04-12', 'price': 340}]
sorted_datav = sorted(datav, key=lambda x: x['price'])
print(f"近三个月前往{ArrCity}的低价机票前三名分别是:\n"
      f"\t{sorted_datav[0]["date"]}\t价格为{sorted_datav[0]["price"]}元\n"
      f"\t{sorted_datav[1]["date"]}\t价格为{sorted_datav[1]["price"]}元\n"
      f"\t{sorted_datav[2]["date"]}\t价格为{sorted_datav[2]["price"]}元\n"
      )




