from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(60)
driver.find_element(By.XPATH,value='//*[@id="langSelect-ZH-CN"]').click()
time.sleep(20)

while True:
    driver.find_element(By.XPATH,value='//*[@id="bigCookie"]').click()
    time.sleep(6)
    
    print(driver.find_element(By.ID,value='cookies').text)
    # print(driver.find_element(By.ID,value='products').find_elements(By.ID,value='productPrice0')[0].text)
#位置数量//*[@id="cookies"]

input()