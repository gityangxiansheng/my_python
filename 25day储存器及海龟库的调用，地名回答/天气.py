# "C:\下载\25 - Day 25 - Intermediate - Working with CSV Data and the Pandas Library\002 weather-data.csv"
# with open(r"C:\下载\25 - Day 25 - Intermediate - Working with CSV Data and the Pandas Library\002 weather-data.csv",mode="r",encoding="utf-8") as ss:
#     sss = ss.readlines()
#     print(sss)

# import csv    
# temp=[]
# with open(r"C:\下载\25 - Day 25 - Intermediate - Working with CSV Data and the Pandas Library\002 weather-data.csv",mode="r",encoding="utf-8") as ss:
#     data = csv.reader(ss)
    
#     for row in data :
#         if not "temp" in row:
#             print(row)
#             temp.append(int(row[1]))
# print(temp)


import pandas as pd

data=pd.read_csv(r"C:\下载\25 - Day 25 - Intermediate - Working with CSV Data and the Pandas Library\004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
# temp_list = data["temp"].to_list()
# print(data["temp"].max())
# data[data["day" == "Monday"]]
# print(data[data.day == "Monday"])
# print(data.condition == "Rain")
# print(data[data.day == "Monday"].temp*1.8+32) 
gray_list=len(data[data["Primary Fur Color"]=="Gray"])
Blak_list=len(data[data["Primary Fur Color"]=="Black"])
Cinnamon_list=len(data[data["Primary Fur Color"]=="Cinnamon"])


dict_color={
    "color":["Gray","Black","Cinnamon"],
    "data" :[gray_list,Blak_list,Cinnamon_list]
}
datas = pd.DataFrame(dict_color)
print(datas)
# datas.to_csv(r"C:\下载\25 - Day 25 - Intermediate - Working with CSV Data and the Pandas Library\004 2018-Central-Park-Squirrel-Census-Squirrel-Data1.csv")

# print(datas)

    
