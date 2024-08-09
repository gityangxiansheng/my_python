name=[name1+0 for name1 in range(1,21)]
print(name)
#使用一个for 循环打印数字1~20
name=list(range(1,21))
print(name)
#使用一个for 循环打印数字1~20
name=[]
for names in range(1,21):
    name.append(names)
print(name)
#使用一个for 循环打印数字1~20

name1=list(range(1,1000001))
print(min(name1))
print(max(name1))
print(sum(name1))
#创建一个列表，其中包含数字1~1 000 000,再使用min() 和max() 核实该列表确实是从1开始，到1 000 000结束的

name2=list(range(3,31,3))
for name2s in name2:
    print(name2s)
#创建一个列表，其中包含3~30内能被3整除的数字；再使用一个for 循环将这个列表中的数字都打印出来。
name3ss=[]
name3=list(range(1,11))
for name3s in name3:
    print(name3s**3)
    name3ss.append(name3s**3)
print(name3ss)

name3ss=[name3s**3 for name3s in range(1,21)]
print(name3ss)
#将同一个数字乘三次称为立方。例如，在Python中，2的立方用2**3 表示