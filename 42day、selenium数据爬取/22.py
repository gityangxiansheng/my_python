from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
datas = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
txt = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")
deta = {}
for _  in range(len(datas)):
    deta[_]={datas[_].text:txt[_].text}
    
print(deta)


input("回车键结束") 