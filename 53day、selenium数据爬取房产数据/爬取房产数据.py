import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


driver = webdriver.Chrome()
driver.get('https://appbrewery.github.io/Zillow-Clone/')

datas = driver.find_elements(By.CSS_SELECTOR,".ListItem-c11n-8-84-3-StyledListCardWrapper")

print(datas)
print(len(datas))
dri = {}
价格 = {}
地址 = {}
网址 = {}
for _ in range(len(datas)):
    价格[_] =datas[_].find_element(By.CSS_SELECTOR,'span').text.replace("/mo","").replace("1 bd","").replace(" ","").replace("1bd","")
    网址[_] =datas[_].find_element(By.CSS_SELECTOR,"a").get_attribute('href')
    地址[_] =datas[_].find_element(By.CSS_SELECTOR,"address").text
dri = {
    "价格" : 价格,
    "地址" : 地址,
    "网址" : 网址,
}
dcc = pd.DataFrame(dri)
print(dcc)
cc = r"python\53day\爬取房产数据.xlsx"
dcc.to_excel(cc)
print(dcc)
input()