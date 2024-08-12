name="yangruixiang"
name=name.upper()
print(name)
name=name.lower()
print(name)
name=name.title()
print(name)
#大小写的转换

name="   yangruixiang   "
print("头"+name+"尾"+"没加格式")

name1=name.rstrip()
print("头"+name1+"尾"+"尾格式")

name2=name.lstrip()
print("头"+name2+"尾"+"头格式")

name3=name.strip()
print("头"+name3+"尾"+"头尾空格")