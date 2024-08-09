# #名称生成器?项目1
# name=input("请输入你的姓名:\n")
# name1=input("请输入你最喜欢的小动物:\n")
# name2=input("请输入你最喜欢的城市:\n")
# print(name[0]+name1[-1]+name2[0])

#字符长度计算？项目2
# print( len(input(" 你的名字叫什么? ") ) )

# #ab小游戏？项目3
# a=input("a=")
# b=input("b=")

# print("a="+a)
# print("b="+b)
# c=a
# a=b
# b=c
# print("a="+a)
# print("b="+b)

# #AA计算器？项目4
# print("欢迎使用AA计算器！")
# spend=float( input("今日消费金额\t:¥") )
# peiple=int( input("均摊人数\t:") )
# tip=int(input("付出小费百分比10-20\t:"))
# tip=tip/100
# jieg=format((spend/peiple+spend/peiple*tip),'.1f')
# print("你需要付出\t¥"+jieg)

# #数字拆分重组？项目5
# tow=input("请输入一串数字：")
# print(type(tow))
# print( int (tow[0]) + int (tow[1]))
# print( int (str( tow[0] ) ) + int ( str( tow[1] ) ) ) 

# 体脂计算器？项目6
# cm=float(input("请输入你的身高单位cm：\n"))
# kg=float(input("请输入你的体重单位kg：\n"))
# m=int(cm)/100
# BMI=float((int(kg)/m**2))
# print(format(BMI,".1f"))
# BMI=34.9
# if BMI >= 18.5 and BMI <= 24.9:
#     print("您现在体重正常！")
# elif BMI < 29.9:
#     print("你太胖了，少吃主食，多运动！！")
# elif  BMI<= 34.9:
#     print("你超重了！")
# elif  BMI >= 35 :
#     print("你太重了需要治疗！")
# else :
#     print("你太瘦了，多吃主食，多运动！！")

# #时间计算器项目7
# age=input("你今年多大了？\n")
# nian=90-int(age)
# yue=nian*12
# day=nian*365
# print(f"你还剩余约{nian}年，{yue}月，{day}日")

# #是偶数吗？项目8
# tow =float ( input ( "请输入一个数字：" ) ) 
# tow1=int(tow)
# if tow != tow1:
#     print("您的输入有误，请输入整数，不要输入浮点数!")
# else:
#     if tow1 % 2 == 0:
#         print(str(tow1)+"是一个偶数")
#     else :
#         print(str(tow1)+"是一个奇数")


# #闰年计算器项目9
# year=int(input("你要查那一年？"))
         
# if year % 4 ==0:

#     if year % 100 ==0:
         
#         if year % 400 ==0:
#             print("算法1"+str(year)+"闰年")
#         else:
#             print("算法1"+str(year)+"not闰年")
#     else:
#         print("算法1"+str(year)+"闰年")
# else:
#     print("算法1"+str(year)+"not闰年")




# #景区计价器？项目10
# #票价1
# Price1=5
# #票价2
# Price2=7
# #票价3
# Price3=12
# variable=""
# cm=int(input("您的身高多是？cm："))
# if cm > 120 :
#     age=int(input("你今年多少岁了？"))
#     if age <= 12 :
#         variable=Price1
#     elif age <= 18:
#         variable=Price2
#     else:
#         variable=Price3
# else:
#     variable="对不起，您的身高不符合安全限制！"

# yes_no=input("您是否愿意和您的门票合照，但是需要支付3美元。yes or no")

# if yes_no.lower() == "yes":
#     print("您本次的消费一共是："+str(3+variable))
# else:
#     print("您本次的消费一共是："+str(variable))

# #景区计价器？2
# #票价1
# Price1=5
# #票价2
# Price2=7
# #票价3
# Price3=12
# variable=0
# cm=int(input("您的身高多是？cm："))
# if cm > 120 :
#     age=int(input("你今年多少岁了？"))
#     # variable=Price1 if age <= 12 else(Price2 if age <=18 else Price3)
#     if age <= 12 :
#         variable=Price1
#     elif age <= 18:
#         variable += Price2
#     elif age >= 45 and age <= 55 :
#         print("一切都会过去的！")
#     else:
#         variable += Price3
# else:
#     variable="对不起，您的身高不符合安全限制！"

# yes_no=input("您是否愿意和您的门票合照，但是需要支付3美元。yes or no")

# if yes_no.lower() == "yes":
#     print("您本次的消费一共是："+str(3+variable))
# else:
#     print("您本次的消费一共是："+str(variable))

# #蛋糕房计价器项目11
# name="小白"
# ml_material=3
# s_material=2
# fruit=1
# cake_s=15
# cake_m=20
# cake_l=25
# money=0
# print("欢迎光临"+name+"蛋糕房!")
# Cake_sml=input("你需要什么型号的蛋糕？s="+str(cake_s)+"元,m="+str(cake_m)+"元,l="+str(cake_l)+"元?:")
# Cake_material=input("你需要加一些夹层奶油吗？如果需加大约"+str(s_material)+"元至"+str(ml_material)+"，n or y：")
# Cake_fruit=input("你需要加一些水果吗？如需要加则需另加"+str(fruit)+"元，n o ry：")
# if Cake_sml.lower() == "s":
#     money+=cake_s
# elif Cake_sml.lower() == "m":
#     money+=cake_m
# elif Cake_sml.lower() == "l":
#     money+=cake_l
# else:
#     print("请按照指示回复数字s，m，l，否则计价将不准确。")

# if Cake_material.lower() == "y":
#     if money == cake_s:
#         money += s_material
#     else:
#         money += ml_material
# elif Cake_material.lower() == "n":
#     money += 0
# else:
#     print("请按照指示回复,Y or N,否则计价将不准确。")

# if Cake_fruit.lower() == "y":
#     money += fruit
# elif Cake_fruit.lower() == "n":
#     money += 0
# else:
#     print("请按照指示回复,Y or N,否则计价将不准确。")
# print("你本次共消费",str(money),"元")



# #爱情计算器项目12
# name1=input("请输入你的英文名：")
# name2=input("请输入他/她的英文名：")
# # name2="rreoli"
# # name1="ttuuuu"
# name=name2.lower()+name1.lower()
# t=name.count("t")
# r=name.count("r")
# u=name.count("u")
# e=name.count("e")
# l=name.count("l")
# o=name.count("o")
# v=name.count("v")
# e=name.count("e")
# true0=(t+r+u+e)
# love=(l+o+v+e)
# love_index=(int(str(true0)+str(love)))
# if love_index < 10 or love_index > 90:
#     print(f"你们的分数是{str(love_index)},你们在一起就像是可乐遇到了曼妥思。")
# elif love_index  > 40 and love_index < 50 :
#     print(f"你们的分数是{str(love_index)},你们在一起很好！")
# else:
#     print(f"你们的分数是{str(love_index)}!") 

# #金银岛小游戏项目13
# print("欢迎来到金银岛，岛上虽然藏着王留下的宝藏，但是时时刻刻伴随着危险，你的任务是找到王留下的宝藏，离开小岛！\n准备好出发了吗？go！go!go!")
# operate1=input("前方有叉路口向左or向右？")
# if operate1 == "向左" :
#     operate2=input("前方有个山洞是or否进去探险？")
#     if operate2 == "否" :

#         operate3=input("前方有个小鳄鱼，是or否尝试收为宠物")
#         if operate3 == "否" :

#             operate4=input("前方有个房子是or否进入查看？")
#             if operate3 == "是" :
#                 print("恭喜！你通关了！")


#             else:
#                 print("抱歉！王的宠物把你咬死了！")
#         else:
#             print("抱歉！小鳄鱼把你咬死了！")        
#     else:
#         print("抱歉！山洞里的大蛇把你咬死了！")    
# else:
#     print("抱歉！路边的毒蛇把你毒死了！")

#猜大小，项目14
# import random 
# print("这是一个筛子游戏，比大小，买定离手！")
# print(f"筛子一号:\t",random.randint(1,10))
# print(f"筛子二号:\t",random.randint(1,10))

# 猜正反，项目15
# print("这是一个抛硬币游戏，猜正反，买定离手！")
# yingb=random.randint(1,11)
# if yingb % 2 == 0 :
#     yingba="正面"
# elif yingb % 2 != 0 :
#     yingba="反面"
# print(f"本次是{yingba}")


# import random #导入随机数模块
# #谁买单？项目16
# 参加饭局的人=input("参加饭局的人的姓名xxx xxx").split()

# 参加人数=len(参加饭局的人)
# 买单的人=参加饭局的人[random.randint(0,参加人数-1)]
# print(买单的人)

# #矩阵挑战项目17
# row1=["1","2","3"]
# row2=["4","5","6"]
# row3=["7","8","9"]
# a=[row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# xx="31"
# column=int(xx[0])-1#列索引为变量xx的第一个字符
# row=int(xx[1])-1#行索引为变量xx的第二个字符
# a[row][column]="x"#根据索引修改值为x
# print(f"{row1}\n{row2}\n{row3}")


# #剪刀石头布
# import random
# # your=input("你输入的1 2 3 分别代表剪刀、石头、布请输入：\n")
# your = "3"
# she = random.randint(1,3)
# a="剪刀"
# b="石头"
# c="布"
# abc = [a,b,c]
# your=int(your)

# if your +1 == she or your - 2 ==she:
#    print("恭喜大魔王！获胜！")
# elif your -1 ==she or your +2 ==she:
#    print("恭喜勇士！获胜！")
# elif your == she :
#    print("平局")
# else:
#    print(your)
#    print(she)

# your = abc[your-1]
# she = abc[she-1]

# print(f"你伸出了{your}")
# print(f"大魔王伸出了{she}")

# #战胜幼年高斯
# b=0
# for a in range(1,101):
#     b += a
#     print(a)
# print(b)

# c=0
# for d in range(0,101,2):
#     if d % 2  ==0:
#         c += d
#         print(d)
# print(c)

# #fizz buzz
# b=[]
# for a in range(1,101):
#     if a % 3 == 0 and a % 5 == 0 :
#         print('fizz buzz')
#     elif a % 3 == 0 :
#         print('fizz')
#     elif a % 5 == 0 :
#         print('buzz')
#     else:
#         print(str(a))
# print(b)

# #密码生成器？
# import random

# 字母 = "a b c d e f g A B C D E F G"
# 数字 = "1 2 3 4 5 6 7 8 9"
# 符号 = "! @ # $ % ^ & * "
# 字母=字母.split()
# 数字 = 数字.split()
# 符号 = 符号.split()
# 字符=[字母+数字+符号]
# 字母长度=len(字母)
# 密码中字母长度=3
# 数字长度=len(数字)
# 密码中数字长度=3
# 符号长度=len(符号)
# 密码中符号长度=3
# 字符长度=len(字符)

# 密码=""
# #简单的密码生成
# # 密码中字符长度=密码中字母长度+密码中符号长度+密码中数字长度
# # for s in range(0,密码中字母长度):
# #     密码=密码+str(字母[random.randint(0,字母长度-1)])
# # for s in range(0,密码中数字长度):
# #     密码=密码+str(数字[random.randint(0,数字长度-1)])
# # for s in range(0,密码中符号长度):
# #     密码=密码+str(符号[random.randint(0,符号长度-1)])

# ##困难的密码生成
# 密码列=[]
# 密码中字符长度=密码中字母长度+密码中符号长度+密码中数字长度
# for s in range(0,密码中字母长度):
#     密码列.append(str(字母[random.randint(0,字母长度-1)]))
# for s in range(0,密码中数字长度):
#     密码列.append(str(数字[random.randint(0,数字长度-1)]))
# for s in range(0,密码中符号长度):
#     密码列.append(str(符号[random.randint(0,符号长度-1)]))
# random.shuffle(密码列)
# for 密码循环 in 密码列:
#     密码=密码+密码循环

# print(密码)

# def greet(name,天气):
#     print(f"你好啊{name}")
#     print(f"今天{天气}很好啊又是快乐的一天")
#     print("今天的Python旅程!")

# greet(天气="杨瑞祥！",name="晴天！")

# #计算墙壁的面积所需的油漆
# import math

# def 公式(wall_height,wall_width,coveragepercan):
#     numberofcans = (wall_height * wall_width) / coveragepercan
#     numberofcans1 = math.ceil(numberofcans)
#     print(f"实际需要{numberofcans}桶,应该购买{numberofcans1}桶！")
# 公式(wall_height=3,wall_width=9,coveragepercan=5)



# # 质数计算器
# def zhishu(x):
#     #结果变量
#     outcome=0
#     #小于等于一，表示不是质数。
#     if  x <= 1:
#         outcome += 1
#     else:
#         for a in range(1,x+1):
#             if x % a == 0:
#                 if a != 1 and a != x:
#                     #outcome>1表示不是质数
#                     outcome += 1
#         if outcome == 0:
#             print(f"{x}是一个质数!")       
#         else:
#             print(f"{x}不是一个质数!")   
# for a in range(0,100):
#     zhishu(a)
