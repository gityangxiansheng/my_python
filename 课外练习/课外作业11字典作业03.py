import os
#定义三个变量键、值、人
def 出现吧():
    dictionary={}
    #创建一个自定义函数：循环添加键值对并自动清空屏幕。
    # def dictionary1():
    #     now_ren1=1
    #     now_ren=""
    #     #循环添加键值对并清空屏幕
    now_ren1= 1   
    now_ren ="yes"
    while now_ren1 > 0:
        if now_ren =="yes":
            key1=input("请输入名字：\n")
            value1=int(input("请输入金额：\n"))
            now_ren=input("是否继续添加人员?yes or no:\n")
            dictionary[key1]=value1
            os.system('cls')
        elif now_ren =="no":
            now_ren1-=2
            # print(dictionary)
        else:
            now_ren1-=2
            print("您的输入有误请重新输入！！")

    获胜者={}
    最大值 = 0
    ## 获取最大值对应的键
    for key, value in dictionary.items():
        # print(type(value))
        if 最大值<value:
            最大值=value
            
    for key, value in dictionary.items():
        if  最大值 == value:
            获胜者[key]=value
    print(获胜者)

出现吧()


    


    