# name = ["yingji","dangjian","dangzheng","zhengfu","bangong","zongzhi"]
# for names in name:
#     if names == "dangjian":
#         print(names.upper())
#     else:
#         print (names.title())
# print(name)


# #示例2不相等条件表达
# name = [1,2,3,4,5,6,7,8,9,10]
# na=0
# for names1 in name:
#     if names1 != 3 :
#         print("他不是数字3！")
#         na = na + 1
# print(na)

# x = 6
# y = 5

# print("x大于y" if x>y else "x小于y")

# name = ["jpc","yyh","yyq","yrx"]
# notname = ["yyy","lijie"]
# names = "nage"
# if names not in notname or names in name :
#     print(names.title()+"你不是黑名单内的，且是正常注册的，欢迎登陆！")



live_car = "BYD"#
like_car = ["Byd","bwm","qy","ad"]
print("你现在的汽车是BYD吗？")
print( live_car == "byd" )

print("\n你现在的汽车是byd吗？")
print( live_car == "BYD" )

print("\n你现在的汽车是你喜欢的汽车，对吗？")
if live_car in like_car :
    print("对")
else:
    print("no")

like_car1 = []

for like_ca in like_car :
    like_car1.append(like_ca.lower().title())
print(like_car1)

live_car=live_car.lower().title()
print(live_car)

print("\n你现在的汽车是你喜欢的汽车，对吗？")
if live_car in like_car :
    print("对")
else:
    print("no")

print("\n你现在的汽车不是以上汽车中的一种对吗？")
if live_car not in like_car :
    print("对")
else:
    print("错")
# print ("我的汽车是比亚迪，对吗？")
print ("\n"+live_car == "BYD")
print ("我的汽车不是比亚迪，对吗？")
print ("\n"+live_car != "BYD")
print ("我的汽车是比亚迪海豚，对吗？")
print ("\n"+live_car == "BYD海豚")

meth=7**7/6/6*3*3/4/4
print("\n"+str(meth>12860 and meth>12867 and meth>=12867))
print(meth)

print("\n"+str(4*4!=6/2))
print("\n"+str(4*4>=6/2))
print("\n"+str(4*4>=6+10))
