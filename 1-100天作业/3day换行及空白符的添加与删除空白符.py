# print("python")#打印python
# print("\tpython")#加\t打印python,有空白符
# print("p\ny\nt\nh\no\nn")#加\n打印python,换行
# print("""p
# y
# t
# h
# o
# n""")#加"""和回车打印python,换行

# name  = "       我是个坚持不懈的人      "
# print (name.rstrip())
# name  = "  我是个坚持不懈的人    "
# print (name.lstrip())


name  = "   我是个坚持不懈的人    "
print ("第一次打印三次"+name+name+name)#打印三次变量
print ("第二次删除尾部空格"+name.rstrip()+name.rstrip()+name.rstrip())#rstrip删除变量尾部空格
print ("第三次删除头部空格"+name.lstrip()+name.lstrip()+name.lstrip())#lstrip删除变量头部空格
print ("第四次删除头尾空格"+name.strip()+name.strip()+name.strip())#strip删除变量头尾空格