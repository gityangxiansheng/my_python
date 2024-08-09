# #5-8 以特殊方式跟管理员打招呼以 
# #5-9 处理没有用户的情形
# html_name=["admin","wantan","001","002","003"]
# if not html_name:
#     print("暂时无人注册登陆！") 
# else:
#     print("目前已有管理员登入！")
#     for html_name1 in html_name:
#         if "admin" in html_name1:
#             print("登陆人："+str(html_name1)+"先生")
#             print("您好！尊敬的"+str(html_name1)+"先生，您要看验证报告吗？")
#         else:
#             print("登陆人："+str(html_name1)+"先生")
#             print("您好！尊敬的"+str(html_name1)+"先生，欢迎登陆！")

# #5-10 检查用户名
# name1=["Admin","Wantan","001","002","003"]
# name1s=[]
# for name1ss in name1:
#     name1s.append(name1ss.lower())
# name2=["dog","py","wantan","admin","001"]

# for name2s in name2:
#     if name2s.lower() in name1s:
#         print("注册用户"+'"'+name2s+'"')
#         print('"'+name2s+'"'+"""该用户名已被使用!""")
#     else:
#         print("注册用户"+'"'+name2s+'"')
#         print('"'+name2s+'"'+"该用户名可用")
# ##豆包修改！
# # 创建包含至少 5 个用户名的列表 name1
# name1 = ["Admin", "Wantan", "001", "002", "003"]

# # 创建一个包含 5 个用户名的列表 name2，并确保其中有一两个用户名也包含在列表 name1 中
# name2 = ["dog", "py", "wantan", "admin", "001"]

# # 创建一个包含 name1 中所有用户名小写形式的列表 name1s
# name1s = [name1ss.lower() for name1ss in name1]

# # 遍历 name2 中的每个用户名，并检查它是否已被使用
# for name2s in name2:
#     if name2s.lower() in name1s:
#         print("注册用户" + '"' + name2s + '"')
#         print('"'+name2s+'"'+ """该用户名已被使用!""")
#     else:
#         print("注册用户" + '"' + name2s + '"')
#         print('"'+name2s+'"'+"该用户名可用")


amx = [ i for i in range(1,10)]
for amx1 in amx:
    if amx1 == 1:
        print("1st")
    elif amx1 == 2:
        print("2nb")
    elif amx1 == 3:
        print("3rd")
    else:
        print(str(amx1)+"th")
        
#豆包生成
amx = [i for i in range(1, 10)]
for amx1 in amx:
    if amx1 == 1:
        print("1st")
    elif amx1 == 2:
        print("2nd")
    elif amx1 == 3:
        print("3rd")
    else:
        print(str(amx1) + "th")