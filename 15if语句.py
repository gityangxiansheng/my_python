# # if 3*4>=12:
# #     print("你真棒棒")
# # else:
# #     print("你真傻逼")

# et_color=["green","yellow","red"]
# if et_color[2]=="green":
#     print("恭喜射杀绿小怪，增加5经验！")
# elif et_color[1]=="green":
#     print("恭喜射杀绿小怪，增加5经验！")
# elif et_color[2]=="green":
#     print("恭喜射杀绿小怪，增加5经验！")
# else:
#     print("恭喜射杀外星人获得10经验")

# et_colors=["green","yellow","red"]
# for et_color in et_colors:
#     print(et_color)
#     if et_color=="green":
#         print("恭喜射杀绿小怪，增加5经验！")
#     elif et_color=="yellow":
#         print("恭喜射杀绿小怪，增加10经验！")
#     elif et_color=="red":
#         print("恭喜射杀绿小怪，增加15经验！")

age=65
if age<2 :
    print("婴儿")
elif age>=2 and age<4:
    print("阑珊学步的宝宝")
elif age>=4 and age<13:
    print("儿童")
elif age>=13 and age<20:
    print("青少年")
elif age>=20 and age<65:
    print("成年人")
else:
    print("中老年人")

like=["香蕉","苹果","梨子"]
if "香蕉" in like:
    print("有香蕉没？")
    print('有的')
    if "苹果" in like:
        print("有苹果没？")
        print('有的')
        if "梨子" in like:
            print("有梨子没？")
            print('有的')

elif "苹果" in like:
    print("有苹果没？")
    print('有的')
elif "梨子" in like:
    print("有梨子没？")
    print('有的')
