import requests
from datetime import datetime
#第一大块创建###
#定义常量用户及用户密码
US = ""
USKEY = ""
#初始化url
pixela_endpoint = ""
#初始化请求内容
user_params = {
    "token" : , 
    "username" : US,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}
# #发送请求并获取返回内容   #创建账户并打印response
# response = requests.post(url=pixela_endpoint,json=user_params)
# #打印返回内容
# print(response.text)

#第二大块定义内容###
#初始化graphs_url
graphs_endpoint = f"{pixela_endpoint}/{US}/graphs"

#初始化请求
graphs_params = {
    "token" : USKEY,
    "id" : US,
    
    "name" : "测试图像",
    "unit" : "Km",
    "type" : "int",
    "color" : "shibafu",
    "timezone" : "Asia/Shanghai"    
}
headers = {
    "X-USER-TOKEN" : USKEY
}
#发送请求，获取数据
# response = requests.post(url=graphs_endpoint,json=graphs_params,headers=headers)
# print(response.text)

#第三大块开始创建像素

#定义url
Pixel_endpoint = f"{pixela_endpoint}/{US}/graphs/{US}"

#获取时间
now_tim = datetime.now()
now = now_tim.strftime("%Y%m%d")
print(now)
ss = input("今天运动了几公里？")
#初始化请求
pixel_params = {
    "date" : now,
    "quantity" : ss,
}
#发送请求，获取数据
responses = requests.post(url=Pixel_endpoint,json=pixel_params,headers=headers)
print(responses.text)


