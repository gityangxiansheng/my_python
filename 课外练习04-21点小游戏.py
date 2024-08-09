import random
#发牌器
def Dealer():
    card =[]
    for a in range(1,14):
        if a == 1 :
            card.append("A")
        elif a == 11 :
            card.append("J")
        elif a == 12 :
            card.append("Q")
        elif a == 13 :
            card.append("K")
        else:
             card.append(str(a))
    return(card[random.randint(0,12)])

#牌面计算器
def operation(mys):
    mysss=0
    myss=0
    for a in mys:
        
        # print(type(a))
        # print(a)
        if a == "A" :
            mysss += 11
        elif a == "J" :
            mysss += 10
        elif a == "Q" :
            mysss += 10
        elif a == "K" :
            mysss += 10
        elif a == "1":
            mysss += 1
        else:
           mysss += (int(a))

    if mysss > 21 and "A" in mys:
        for a in mys:
            if mysss > 21 and "A" in mys:
               mys.remove("A")
               mys.append("1")
    for a in mys:
        
        # print(type(a))
        # print(a)
        if a == "A" :
            myss += 11
        elif a == "J" :
            myss += 10
        elif a == "Q" :
            myss += 10
        elif a == "K" :
            myss += 10
        elif a == "1":
            myss += 1
        else:
            myss += (int(a))    
    return myss
#我的比较公式
def compare(chooses):
    mys=[]
    computers=[]
    #输入列表求和！
    my_sum=operation(mys)
    computer_sum = operation(computers)
    # print(my_sum)
    # 如果我的总数>21choose参数代表胜利或者失败！
    # chooses= input("您要开始21点扑克游戏吗？1.开始 2.结束")

    for _ in range(0,2):
        computers.append(Dealer())
        computer_sum = operation(computers)
        mys.append(Dealer())
        my_sum=operation(mys)
    print("你当前的牌面:",mys,"当前点数：",my_sum)
    print("电脑当前的牌面:",computers,"当前点数",computer_sum)

    if my_sum <= 21 and chooses == "1" and len(mys) == 2:
        while my_sum <= 21 and chooses == "1":
            chooses=input("继续抽牌请按1；停止抽牌请按2:\n")
            if chooses == "1":
                mys.append(Dealer())
                my_sum=operation(mys)
                # print(my_sum)
                print("你当前的牌面:",mys,"当前点数：",my_sum)
                print("电脑当前的牌面:",computers,"当前点数",computer_sum)
            elif chooses == "2":
                my_sum=operation(mys)
                # print(my_sum)
                print("你当前的牌面:",mys,"当前点数：",my_sum)
                print("电脑当前的牌面:",computers,"当前点数",computer_sum)
    elif my_sum > 21 :
        lose="2"#玩家爆炸
        print("#玩家爆炸")  
    else :
        print("电脑抽牌")
        print("你当前的牌面:",mys,"当前点数：",my_sum)
        print("电脑当前的牌面:",computers,"当前点数",computer_sum)
    #如果机器的牌面<=16，增加电脑一张牌
    if computer_sum <= 16:
        while computer_sum <= 16:
            computers.append(Dealer())
            computer_sum = operation(computers)
            print("电脑当前的牌面:",computers,"当前点数",computer_sum)
            if computer_sum > 21:
                lose="1"#电脑爆炸
            elif computer_sum <= 21:
                if computer_sum>my_sum:
                    lose="3"#电脑胜利
                elif computer_sum<my_sum:
                    lose="4"#我胜利
                elif computer_sum == my_sum:
                    lose="5"#平局！
    elif computer_sum <= 21:
        if computer_sum>my_sum:
            lose="3"#电脑胜利
        elif computer_sum<my_sum:
            lose="4"#我胜利
        elif computer_sum == my_sum: 
            lose="5"#平局！
    return lose   
chooses= input("您要开始21点扑克游戏吗？1.开始 2.结束\n")
a="y"

while a=="y":
    lose=compare(chooses)
    if lose == "1":
        print("电脑爆炸了，你胜利了！！")
    elif lose == "2":
        print("你爆炸了，超过21点了！")
    elif lose == "3":
        print("你输了！电脑的分数超过你了！")
    elif lose == "4":
        print("你胜利了！！！")
    elif lose == "5":
        print("平局了！！！")
    a=input("你要继续游戏吗？y or n")
    if a=="n":
        print("游戏结束")   
