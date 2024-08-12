#1定义加减乘除公式！
#+
def add (n1,n2):
    return n1+n2
#-
def subtract (n1,n2):
    return n1-n2
#*
def multiply(n1,n2):
    return n1 * n2
#/
def divide(n1,n2):
    return n1 / n2

##将加减乘除符号，及公式添加到字典
operation={
"+":add,
"-":subtract,
"*":multiply,
"/":divide
}
# print(operation)

#定义循环打印一遍运算符的公式
def print1():
    for operations in operation:
        print(operations)

#定义从字典中取出运算符公式并使用
def operations1(n3,n1,n2):
    for operations in operation:
        if n3 == "+" or n3 == "-" or n3 == "*" or n3 == "/":
           if operations == n3:
                answer=operation[operations](n1,n2)
                return answer
        else:
            # print("您的输入有误!")
            return "您的输入有误!"

#输入数据
n1 = int(input("请输入数字！"))#输入第一个运算数据
print1()#打印运算符
n3 = input("请输入+ - * /")#输入运算符
n2 = int(input("请输入数字！"))#输入第二个运算数据

# n1 = 3
# n2 = 2
# n3 = "*"
#以上为调试用输入

#调用字典取出运算符函数，加运算公式函数计算出计算结果
answer=operations1(n3,n1,n2)
answers=answer

#如果运算符没有输入错误就打印公式及结果，如果输入错误打印您的输入有误！
if operations1(n3,n1,n2) == "您的输入有误!":
    print("您的输入有误!")
else:
    print(f"{n1} {n3} {n2} = {answer}")
    n4 = input("是否继续计算？")#请输入是否继续计算y n。

    while n4 == "y":#如果输入y
        print1()#打印运算符
        n3 = input("请输入+ - * /") #输入运算符
        n5 = int(input("请输入数字！"))#输入第二个数据
        answers=answer#重新定义上次运算的和，防止覆盖。
        answer=operations1(n3,answer,n5)##调用字典取出运算符函数，加运算公式函数计算出计算结果
        print(f"{answers} {n3} {n5} = {answer}")
        n4 = input("是否继续计算？")
    




        