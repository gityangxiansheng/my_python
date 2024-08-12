surname=( "yang" )
name=("rui xiang")
sentence=("hi!"+" "+ name+" "+surname+" "+"早上好！")
print(sentence)#将用户的姓名存到一个变量中，并向该用户显示一条消息。

surname=("YanG")
name=("rUi xIang")
print(surname+" "+name)#打印一个名字
surname=surname.lower()
name=name.lower()
Name=surname.title()+" "+name.title()
print(Name)
Name=Name.upper()
print(Name)#运用title()+lower()+upper()改变文字大小写。
#将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名。

print("""Albert Einstein oncesaid,“Apersonwho never madea mistake never tried anything new.”""")
#找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出来。

famous_person="Albert Einstein"
message='oncesaid,“Apersonwho never madea mistake never tried anything new.”'
print(famous_person+" "+message)
#重复练习2-5，但将名人的姓名存储在变量famous_person 中，

now_name="yang rui xiang"
now_name1="\n\t"+now_name+"\n\t"
print(now_name1)
print("头"+now_name1.rstrip()+"尾")
print("头"+now_name1.lstrip()+"头")
print("头"+now_name1.strip()+"空")
# 存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t" 和"\n" 各一次。
# 打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数lstrip() 、rstrip() 和strip() 对人名进行处理，并将结果打印出来。