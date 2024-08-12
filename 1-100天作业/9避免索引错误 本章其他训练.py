name=[]
name.append("f泰山")
print("列表内添加泰山")
name.append("s嵩山")
print("列表内添加嵩山")
name.append("a黄山")
print("列表内添加黄山")
name.append("g华山")
print("列表内添加华山")
name.insert(0,"b北京")
print("列表索引为0的地方添加北京")
print(name)
print(sorted(name))
print("按照字母排序当前列表")
print(sorted(name,reverse=True))
print("按照字母反向排序")

print("想去的地方一共有"+(str(len(name)))+"个")

# name_not=[]
# print(name)
# name_not=name.pop(0)
# print(name)
# print(name_not)
# print("通过pop命令移动name列表内的第0个索引到name_not")

# print(name)
# name_not=["b北京"]
# name.remove(name_not[0])
# print(name)
# print(name_not)
# print("通过remove命令移动name列表内的第0个索引到name_not")


# print(name[5])
# #索引错误训练,索引是从0开始的，所以这里的5并不存在。
# name2=[]
# print(name2[-1])
# #索引错误训练,空列表时候name2[-1]会报错。


print("本练习用到的命令有print,pop,remove,len,sorted,sourted(reverse=true),str")