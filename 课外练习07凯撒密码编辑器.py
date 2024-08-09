def caesar(index,input11,yesoron) :
    if yesoron == "yes":
        index=index
    else:
        index=(-index)
    index2=""#解密输出变量
    #字母表
    list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    list2=[]#转换后的字母表变量
    #重新制作一个列表list2，切片久列表中密码以前的项目添加到新列表，然后切片旧列表中密码以后的项目添加到新列表中。
    for a in  list1[index:]:
        list2.append(a)
    for a in  list1[:index]:
        list2.append(a)
    #遍历输入变量，如果输入变量的字符存在于列表1中，安装变量中字符在列表1中的位置，取出列表2中的字符添加到新变量中。
    for input111 in input11:
        if input111 in list2 :
            index2 += list2[list1.index(input111)]
    #如果输入变量的字符不存在于列表1中，则不参加取放操作直接添加到新变量中。
        else:
            index2 += input111
    print(f"您获得的密码为{index2}")
yesoron1=1
while yesoron1 == 1:
    a=input("加密yes or 解密 no：\n")
    list2=input("需要加密的内容:\n")
    c=int(input("需要加密的位数:\n"))
    caesar(index=c,input11=list2,yesoron=a)
    yesoron=(input("你是否要结束程序？yes or no ：\n"))
    if yesoron == "no":
        yesoron1 = 1
    elif yesoron == "yes":
        yesoron1 += 1
        print("程序已结束！")

        


# a=input("加密yes or 解密 no：\n")
# list2=input("需要加密的内容:\n")
# c=int(input("需要加密的位数:\n"))
# caesar(index=a,input11=list2,yesoron=c)



