import requests 
from datetime import datetime  
from dateutil.relativedelta import relativedelta  

url = "https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=python&city=101180100&experience=&payType=&partTime=&degree=&industry=&scale=&stage=&position=&jobType=&salary=&multiBusinessDistrict=&multiSubway=&page=1&pageSize=30"
headers={
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cookie':'',
    'Referer':'https://www.zhipin.com/web/geek/job?query=python&city=101180100',
    'Sec-Fetch-Site':'same-origin',
}
datas = requests.get(url=url,headers=headers).json()

print(datas)
    






