name=["苹果","香蕉","梨子","橙子","橘子"]
print("最喜欢水果排行前三位分别是"+str(name[:3]))
print("最喜欢水果排行中间三位分别是"+str(name[1:3]))
print("最喜欢水果排行后三位分别是"+str(name[-3:]))

names=name[:]
names.append("葡萄")
name.append("提子")
print("我最喜欢的水果有"+str(name))

for namess in  names:
    print("我最喜欢的水果有"+namess)

