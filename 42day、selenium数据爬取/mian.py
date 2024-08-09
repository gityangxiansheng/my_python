from  selenium import webdriver
from selenium.webdriver.common.by  import By


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach",False)

driver = webdriver.Chrome()

driver.get("https://movie.douban.com/chart")
ssc = driver.find_elements(By.CLASS_NAME,value="pl2")
for ss_ in ssc:
    print(f"电影名字：{ss_.find_element(By.TAG_NAME,value="a").text}\n")
    print(f"幕后：{ss_.find_element(By.TAG_NAME,value="p").text}\n")
    print(f"评分：{ss_.find_element(By.CLASS_NAME,value="rating_nums").text}\n")
    print(f"链接：{ss_.find_element(By.TAG_NAME,value="a").get_attribute("href")}\n")



input("回车关闭")

