
# #一个奇怪的计价作业？
# print("welcome to the rollercoaster")
# cm=int(input("你的身高多少cm？"))
# mp0=5
# mp1=7
# mp2=12

# if cm > 120 :
#     age=int(input("您的年龄多大了？"))
#     if age<12:
#         print("你的门票"+str(mp0)+"元")
#         yes_no=input("你是否要和您的门票合影？yes or no")
#         yes_no1=yes_no.lower()
#         zp=3
#         if yes_no == "yes" :
#             print("您本次的消费共计"+str(mp0+zp))
#         elif yes_no == "no": 
#             print("您本次的消费共计"+str(mp0)) 
#     elif age <= 18:
#         print("你的门票"+str(mp1)+"元")
#         yes_no=input("你是否要和您的门票合影？yes or no")
#         yes_no1=yes_no.lower()
#         zp=3
#         if yes_no == "yes" :
#             print("您本次的消费共计"+str(mp1+zp))
#         elif yes_no == "no": 
#             print("您本次的消费共计"+str(mp1))        
#     else:
#         print("你的门票"+str(mp2)+"元")
#         yes_no=input("你是否要和您的门票合影？yes or no")
#         yes_no1=yes_no.lower()
#         zp=3  
#         if yes_no == "yes" :
#             print("您本次的消费共计"+str(mp2+zp))
#         elif yes_no == "no": 
#             print("您本次的消费共计"+str(mp2))  
# else:
#     print("不好意思，你的身高不够")





# #披萨店？
# print("欢迎来到纯正意大利风味披萨店！！")
# size=input("你需要多大的披萨 S,M,L?")
# add_penpperoni=input("你是否需要额外添加香肠？3元。Y,N")
# extra_cheese=input("你是否需要添加额外的奶酪？Y,N:")
# money=0
# Small_Pizza=15
# Medium_Pizza=20
# Large_Pizza=25
# if size.lower() == "s":
#     money += Small_Pizza
# elif size.lower() == "m":
#     money += Medium_Pizza
# elif size.lower() == "l":
#     money += Large_Pizza
# else:
#     print("由于我是一个程序，您可能需要按照正确的提示进行输入！！")
# if add_penpperoni.lower() == "y":
#     if str(money) == "15": 
#         money += 2
#     else:
#         money += 3
# else:
#     money += 0
# if extra_cheese.lower() == "y":
#     money = money + 1
# else:
#     money += 0
# print("您本次一共消费："+str(money)+"元")

# #抛硬币
# import random

# print("让我们将命运的硬币抛向天空！")
# input("倒数3：")
# input("倒数2：")
# input("倒数1：")
# a=random.randint(1,11)
# if a % 2 == 0 :
#     print("正面")
# else:
#     print("反面")


# # #左轮买饭
# import random

# names_string = input ("参加游戏的人的名字分别是：")
# names = names_string.split(",")


# person_who_will_pay = random.choice(names)
# print(person_who_will_pay,"公子买单！")

# # a=len(names)
# # print(names[random.randint(0,a-1)],"公子买单！")


# #棋盘
# row1 = ["1","2","3"]
# row2 = ["4","5","6"]
# row3 = ["7","8","9"]
# map = [row1,row2,row3]
# # print(f"{row1}\n{row2}\n{row3}")
# position=input("你想把宝藏放在那里?")
# print(position[0])
# print(position[1])
# a=map[int(position[1])-1][int(position[0])-1]="x"
# print(a)

# # print(position[0])
# # print(position[1])
# # if position[0] == "1":
# #     a=row1
# # elif position[0] == "2": 
# #     a=row2
# # elif position[0] == "3": 
# #     a=row3
# # else:
# #     print("超出索引！")
# # if position[1] == "1" :
# #     a[0]="x"
# # elif position[1] == "2" :
# #     a[1]="x"
# # elif position[1] == "3" :
# #     a[2]="x"
# # else:
# # #     print("超出索引！")

# print(f"{row1}\n{row2}\n{row3}")



# #剪刀石头布游戏
# import random
# x = 0

# while x <= 19:
#     print(f"第{x+1}局游戏开始")
#     x += 1    
#     Rock="""
#             _______    
#         ---'   ____)   
#                 (_____)  
#                 (_____)  
#                 (____)   
#         ---.__(___)    
#     """
#     paper="""                     
#         _______        
#     ---'   ____)____   
#                 ______)  
#                 _______) 
#             _________)  
#     ---.____________)    
#     """
#     scissors="""                     
#         _______        
#     ---'   ____)____   
#                 ______)  
#             __________) 
#             (____)       
#     ---.__(___)        
#     """                     
#     rps=[scissors,Rock,paper,]
#     a=input("请输入1，2，3，或者剪刀，石头，布，和我对战一局吧！")
#     if a == "1" or a == "剪刀":
#         a=0
#     elif a == "2" or a == "石头":
#         a=1
#     elif a == "3" or a == "布":
#         a=2
#     else:
#         print("您的输入有误，请重新输入！")
#         continue
    
#     my=rps[a]
#     yours=(random.randint(0,2))
#     your=rps[yours]
#     print(f"你伸出了{my}\n")
#     print(f"\n大魔王伸出了{your}")
    

#     if a == yours :
#         print("平局啦！")
#     elif (a == 0 and yours==1)or(a == 1 and yours==2)or(a == 2 and yours==0):
#         print("你输了")
#     elif (a == 2 and yours==1)or(a == 0 and yours==2)or(a == 1 and yours==0):
#         print("你胜利了！！！！")
#     else:
#         print("程序出问题了？")


# #求平均值？？

# student_heighets=input("请输入学生身高").split()

# for n in range(0,len(student_heighets)):
#     student_heighets[n]=int(student_heighets[n])
# print(student_heighets)

# a=0
# sum1=0
# for student_heighets_1 in student_heighets:
#     a+=1
#     print(a)
#     sum1+=student_heighets_1
#     print(sum1)
# print(a)
# print(sum1)
# Average=sum1/a
# print(Average)


#求最高值？？

# student_heighets=input("请输入学生身高").split()

# for n in range(0,len(student_heighets)):
#     student_heighets[n]=int(student_heighets[n])
# print(student_heighets)

# big=0
# liltie=999999999
# for student_heighets_1 in student_heighets:
#     if student_heighets_1 > big :
#         big=student_heighets_1
#     else:
#         big = big 
#     if student_heighets_1 < liltie :
#         liltie=student_heighets_1
#     else:
#         liltie = liltie 
# print("最大的",big)
# print("最小的",liltie)


# #相加
# total=0
# for number in range(1,101):
#     total+=number
# print(total)

# #偶数相加
# total=0
# for number in range(2,101,2):
#     total+=number
#     print(total)

# #fizzbuzz
# a=0
# for s in range(1,101):
#     if s % 5 == 0 and s % 3 ==0:
#         s = "buzzfizz"
#     elif s % 5 == 0 :
#         s = "buzz"
#     elif s % 3 == 0 :
#         s = "fizz"
#     else:
#         s = s
#     print(s)

# ##密码生成器
# import random
# letters="a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
# numbers="1 2 3 4 5 6 7 8 9"
# soymbols="! # $ % & ( ) * +"
# letterss=letters.split( )
# numberss=numbers.split( )
# soymbolss=soymbols.split( )
# print("欢迎来到密码生成器！")
# # nr_letters=int(input("你的密码中应该有多少个字母？"))
# # nr_numberss=int(input("你的密码中应该有多少个数字？"))
# # nr_soymbolss=int(input("你的密码中应该有多少个符号？"))
# nr_letters=int("3")
# nr_numbers=int("3")
# nr_soymbols=int("3")
# mima=""
# lettersss=len(letterss)-1
# numbersss=len(numberss)-1
# soymbolsss=len(soymbolss)-1
# #简单的生成器：
# for nr_letter in range(0,int(nr_letters)):
#     mima=mima+letterss[random.randint(0,lettersss)]


# for nr_number in range(0,int(nr_numbers)):
#     mima=mima+numberss[random.randint(0,numbersss)]


# for nr_soymbol in range(0,int(nr_soymbols)):
#     mima=mima+soymbolss[random.randint(0,soymbolsss)]

# print(mima)

# #复杂的生成器！
# character=[letterss,numberss,soymbolss]#列表融合成1个
# sums=[nr_letters,nr_numbers,nr_soymbols]#迭代数量
# sums=sum(sums)
# for sumss in range(0,sums*4):#迭代次数0-100次
#     if sums > 0:#判断是否还需要新增密码位数
#         a = character[random.randint(0,2)]
#         if a == numberss:
#             if nr_numbers > 0 :#判断是否还需要增加数字密码
#                 mima += numberss[random.randint(0,numbersss)]#如果需要的话增加1位随机数字密码
#                 nr_numbers -= 1 #所需位数-1
#             else:
#                 print("当前数字密码已满")

#         elif a == letterss:
#             if nr_letters > 0: #判断是否还需要增加字母密码
#                 mima += letterss[random.randint(0,lettersss)]#如果需要的话增加1位随机字母密码
#                 nr_letters -= 1 #所需位数-1
#             else:
#                 print("当前字母密码已满")

#         elif a == soymbolss:
#             if nr_soymbols > 0:#判断是否还需要增加符号密码
#                 mima += soymbolss[random.randint(0,soymbolsss)]
#                 nr_soymbols -= 1
#             else:
#                 print("当前符号密码已满")

#     else:
#         print(mima)


    # elif nr_letters == 0:
    #     a =character[random.randint(0,2)]
    #     if a == letterss:
    #         print("跳过本列表")
    #     elif a == numberss:
    #         mima += numberss[random.randint(0,numbersss)]
    #         nr_numbers-=1
    #         print(mima)
    #         print(a)
    #         print("密码+1")
    #     elif a == soymbolss:
    #         mima+=soymbolss[random.randint(0,soymbolsss)]
    #         nr_soymbols-=1
    #         print(mima)
    #         print(a)
    #         print("密码+1")
    #     else:
    #         print("cuow")

    
# print(mima)
#玩家输入
gamer=""

#行刑者输入变量，及转换后的列表
Executioner=input("请行刑官输入您的字符：")
Executioner_lisi=[]
Executioner1_lisi=[]
for Executioners_lisi in Executioner:
    Executioner_lisi.append(Executioners_lisi)
    Executioner1_lisi.append(Executioners_lisi)

#下划线
mystery=["_"]*len(Executioner_lisi)
# print(mystery)

#循环变量设置
round1=0
#胜负变量
yesoron=0
#循环7次错误机会,正确每次一个字符，写满整个单词或者直接输入正确的整个单词结束循环。
while round1 <=6:
    #玩家输入转列表方便操作
    gamer=input("请输入你的猜测：")
    gamer_lisi=[]
    for gamers in gamer:
        gamer_lisi.append(gamers)

    #判断单次输入数量>=审判数量,判定输入为单词，判断单词是否正确
    if len(gamer)>=len(Executioner) and len(Executioner)> 1 :
        
        if gamer in Executioner:
            yesoron=1
            round1+=7
           
        else:
            print(f"答错了！你还有{str(6-round1)}次机会")
            round1+=1
            if 7-round1 == 0:
                yesoron=2
    
    #如果输入字符包含在词汇中
    elif gamer in Executioner1_lisi:
        #查找词汇位置，替换到下划线列表中
        Character_position=Executioner.index(gamer)
        mystery[int(Character_position)]=gamer
        Executioner1_lisi.remove(gamer)
        print(mystery)
        #如果带下划线列表被填满打印获胜并结束循环
        if mystery == Executioner_lisi:
            round1+=7
            yesoron=1
        # else:
            # print(f"答错了！你还有{}次机会")
    else:
        round1+=1
        print(f"答错了！你还有{str(7-round1)}次机会")
        if 7-round1 == 0:
            yesoron=2
if yesoron == 1:
    print("恭喜你获得胜利")
elif yesoron == 2:
    print("失败了")
else:
    print("出现未知错误！")

