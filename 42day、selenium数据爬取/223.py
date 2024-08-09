from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

opt = Options()
# opt.binary_location =r"C:\Program Files\Google\Chrome\Application\chrome.exe"
service = Service(executable_path=r"42day\chromedriver.exe")
driver = webdriver.Chrome( service=service)
driver.get("https://www.google.com.hk/") 


