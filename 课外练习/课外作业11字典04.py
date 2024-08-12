# import isort
#给包含字典、字典中包含列表、包含字符串、整数的列表内添加字典！
#定义列表
Computer = [
    {
    "my_like":[1, 2, 3],
    "spk":"Hello, world!",
    "vs" : 12
    },
    {
    "my_like":[2, 3, 4],
    "spk":"yes, world!",
    "vs" : 10
    }
]

#自定义函数
def 新的文件(my_like1,spk1,vs1):
    新的字典={}
    新的字典["my_like"]=my_like1
    新的字典["spk"]=spk1
    新的字典["vs"]=vs1
    print(新的字典)
    Computer.append(新的字典)
    print(Computer)
#执行自定义函数
新的文件([4,5,6],"on,world",1)
#Print：computer 打印computer
print(Computer)


