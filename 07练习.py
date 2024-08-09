Guest_list=["yrx","lj","yyh","yyq","jpc","jic"]
invite=("我们搬新家了！"+"真诚的邀请"+str(Guest_list)+"先生们、女士们，来到我家，共庆乔迁之喜！")
print(invite)

Guest_list=["yrx","lj","yyh","yyq","jpc","jic"]
Guest_list_not=Guest_list.pop(3)
Guest_list.append("yqq")
Guest_list.insert(0,"yfz")

Guest_list=["yrx","lj","yyh","yyq","jpc","jic"]
Guest_list_not="yyq"
Guest_list.remove(Guest_list_not)
Guest_list.append("yqq")
Guest_list.insert(0,"yfz")


invite=("我们搬新家了！"+"真诚的邀请"+str(Guest_list)+"先生们、女士们，来到我家，共庆乔迁之喜！")
Did_not_participate=(Guest_list_not)
print(invite)
print("未参加人员"+str(Did_not_participate))

Guest_list=["yrx","lj","yyh","yyq","jpc","jic"]
#变量名单
Guest_list_not="yyq"
Guest_list.remove(Guest_list_not)
#用remove命令把yyq写入not名单
Guest_list.append("yqq")
#用append命令，添加一个字符串yqq
Guest_list.append("yy")
#用append命令，在末尾添加一个字符串yy
Guest_list.insert(0,"yfz")
#使用.insert在首位添加一个字符串yfz
Guest_list.insert(0,"yzz")
#使用.insert在首位添加一个字符串yzz
Guest_list.append("nn")
#用append命令，在末尾添加一个字符串nn
Guest_list_not="yrx"
Guest_list.remove(Guest_list_not)
#用remove命令，列表中的将yrx移动至Guest_list



# invite=("我们搬新家了！"+"真诚的邀请"+str(Guest_list)+"先生们、女士们，来到我家，共庆乔迁之喜！")
# Did_not_participate=(Guest_list_not)
# print(invite)
# print("未参加人员"+str(Did_not_participate))
# print("很抱歉，女士们先生们，由于我的餐桌还为送达，暂时不能邀请你们来到我家共庆乔迁之喜！")


invite=("我们搬新家了！"+"真诚的邀请"+str(Guest_list)+"先生们、女士们，"+str(len(Guest_list))+"人，来到我家，共庆乔迁之喜！")
Did_not_participate=(Guest_list_not)
print(invite)
print("很抱歉，"+Guest_list_not+"，由于我的餐桌还为送达，暂时不能邀请你们来到我家共庆乔迁之喜！")
#正常打印
Guest_list_not=Guest_list.pop()
print("很抱歉，"+Guest_list_not+"，由于我的餐桌还为送达，暂时不能邀请你们来到我家共庆乔迁之喜！")
#用pop命令将列表末尾的字符串移动至not，并打印。

Guest_list_not=Guest_list.pop()
print("很抱歉，"+Guest_list_not+"，由于我的餐桌还为送达，暂时不能邀请你们来到我家共庆乔迁之喜！")
#用pop命令将列表末尾的字符串移动至not，并打印。
Guest_list_not=Guest_list.pop()
print("很抱歉，"+Guest_list_not+"，由于我的餐桌还为送达，暂时不能邀请你们来到我家共庆乔迁之喜！")
#用pop命令将列表末尾的字符串移动至not，并打印。
Guest_list_not=Guest_list.pop()
print("很抱歉，"+Guest_list_not+"，由于我的餐桌还为送达，暂时不能邀请你们来到我家共庆乔迁之喜！")
#用pop命令将列表末尾的字符串移动至not，并打印。
Guest_list_not=Guest_list.pop()
print("很抱歉，"+Guest_list_not+"，由于我的餐桌还为送达，暂时不能邀请你们来到我家共庆乔迁之喜！")
#用pop命令将列表末尾的字符串移动至not，并打印。
Guest_list_not=Guest_list.pop()
print("很抱歉，"+Guest_list_not+"，由于我的餐桌还为送达，暂时不能邀请你们来到我家共庆乔迁之喜！")

Guest_list_not=Guest_list.pop()
print("很抱歉，"+Guest_list_not+"，由于我的餐桌还为送达，暂时不能邀请你们来到我家共庆乔迁之喜！")
#用pop命令将列表末尾的字符串移动至not，并打印。

print("真诚的邀请您！"+str(Guest_list)+"先生与我共进晚餐！")
del Guest_list[0]
#利用del命令删除Guest_list的第一个内容
del Guest_list[0]
#利用del命令删除Guest_list的第一个内容
print("\t\n\n\n"+str(Guest_list))

name=["0","1","2","3","4","5","6","7","8","9"]
name1=[]
name0=name.pop()
print(name)
print(name0)
print(name1)

# name=["0","1","2","3","4","5","6","7","8","9"]
# name1=[]
# name1.append(name.pop(0))
# #将name列表末尾移动到name1列表内
# print(name)
# print(name1)
# name1.append(name.pop(0))
# print(name)
# print(name1)
# name1.append(name.pop(0))
# print(name)
# print(name1)
# name1.append(name.pop(0))
# print(name)
# print(name1)
# name1.append(name.pop(0))
# print(name)
# print(name1)
# name1.append(name.pop(0))
# print(name)
# print(name1)
# name1.append(name.pop(0))
# print(name)
# print(name1)
# name1.append(name.pop(0))
# print(name)
# print(name1)
# name1.append(name.pop(0))
# print(name)
# print(name1)
# name1.append(name.pop(0))
# print(name)
# print(name1)