# import requests
# #城市编码，身份证号前几位。
# city = "410122"
# #密匙
# key = ""
# #气象类型“base”返回实时天气，空值为“base”。
# #气象类型“all”返回预报天气，预报天气每天更新3次，分别在8、11、18点左右更新。
# extensions = "all"
# #返回数据类型“JSON”和“XML”两个，空值为“JSON”。
# output = "JSON"

# ulr=f"https://restapi.amap.com/v3/weather/weatherInfo?city={city}&key={key}&extensions={extensions}&output={output}"

# tianqi = requests.get(ulr)


# ss = tianqi.json()
# print(ss["forecasts"][0]["casts"])





import pandas  as pd
import random 

datt = pd.read_excel(r"python\35day_api_高德天气\zhaichao.xls")
dat_list = datt.values.tolist()
print(random.choice(dat_list)[0])
