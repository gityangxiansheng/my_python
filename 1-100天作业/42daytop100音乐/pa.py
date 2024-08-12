import requests 
from bs4 import BeautifulSoup
import pandas as pd 
import re

url = "https://www.billboard.com/charts/hot-100/2016-06-21/"

dat = requests.get(url).text

# data = BeautifulSoup(dat,"html.parser")

with open(r"python\top100音乐\pa.txt","w",encoding="utf-8") as ccc:
    ccc.write(dat)







# datas = data.find_all(id="title-of-a-story",class_="a-no-trucate")
# #获取歌名
# ff = [str(dat.getText()).replace("\n","").replace("\t","") for dat in datas[0:100]]
# #获取歌手名
# names = data.find_all(name="span" ,class_="a-no-trucate")
# name = [str(_.getText()).replace("\n","").replace("\t","") for _ in names[0:100]]
# print(name)
# print(ff)

# datass={}
# datass["歌手名"] = name
# datass["歌曲名"] = ff
# csd = pd.DataFrame(datass)
# csd.to_excel(r"python\top100音乐\pa.xlsx")


