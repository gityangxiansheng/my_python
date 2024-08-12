import requests 
from bs4 import BeautifulSoup
import time
import pandas as pd
#设置url
lebell = []
ps = []
names = []
for _ in range(11):
    time.sleep(2)
#     #获取响应内容
    url = f"https://ssr1.scrape.center/page/{_}"
    data = requests.get(url=url).text
    datas = BeautifulSoup(data,"html.parser")
    #电影名字
    data = datas.find_all(name="h2")
    name = [da.getText() for da in data]
    names += name
    #评分数据
    data_p = datas.find_all(name="p",class_="score m-t-md m-b-n-sm")
    p = [str(da.getText()).replace("\n                ","") for da in data_p]
    ps += p
    #电影标签
    data_span = datas.find_all(name="div",class_="p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16")
    for _ in data_span:
        lebel = _.find_all(name="span")
        lebels = [ss.getText() for ss in lebel]
        lebell.append(lebels)
dac = {}
dac ["电影名"]= names
dac["评分"] = ps
dac["标签"] = lebell
cx = pd.DataFrame(dac)
cx.to_excel(r"python\爬爬\main.xlsx")
print(cx)
