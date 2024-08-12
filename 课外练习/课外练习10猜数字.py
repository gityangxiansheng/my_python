import random

print("欢迎来到猜数字游戏!请猜出我选择的1-100之间的随机数")
# inputs_猜测次数="困难"
inputs_猜测次数=input("你选择简单还是困难,请回复简单或是困难,开始游戏!\n")
if inputs_猜测次数=="简单":
    inputs_猜测次数s=int(input("你需要几次才能猜对？"))
elif inputs_猜测次数=="困难":
    inputs_猜测次数s=5
else:
    print("请检查你的输入是否有误")
feedback = 0
#创建一个一到一百之间的随机数
numbers = random.randint(1,100)
while not inputs_猜测次数s <= 0:
    
    inputs_猜测数字s=int(input("请输入您猜测的数字:"))
    if inputs_猜测数字s > numbers:
        print("你猜测的数字有点大了")
    elif inputs_猜测数字s < numbers:
        print("你猜测的数字有点小了")
    else :
        inputs_猜测次数s=0
        feedback = 1
    inputs_猜测次数s -= 1
    if inputs_猜测次数s > 0:
            print("再来一次吧")
            print(f"请珍惜你剩余的{inputs_猜测次数s}次机会")

if inputs_猜测次数s <=0  and feedback == 1:
    print("恭喜你答对了!")
elif inputs_猜测次数s <=0  and feedback != 1:
    print(f"正确数字是 ‘{numbers}’ 你未在规定次数内猜到正确的数字，你输了！游戏结束!")
