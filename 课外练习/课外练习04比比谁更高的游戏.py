import random
import os

data = [
  {
    "name": "Instagram",
    "follower_count": 346,
    "description": "社交媒体平台",
    "country": "美国"
  },
  {
    "name": "克里斯蒂亚诺·罗纳尔多",
    "follower_count": 2152,
    "description": "足球运动员",
    "country": "葡萄牙"
  },
  {
    "name": "Facebook",
    "follower_count": 1232,
    "description": "热门社交网络",
    "country": "美国"
  },
  {
    "name": "利昂内尔·梅西",
    "follower_count": 456,
    "description": "著名足球运动员",
    "country": "阿根廷"
  },
  {
    "name": "TikTok",
    "follower_count": 789,
    "description": "短视频平台",
    "country": "中国"
  },
  {
    "name": "勒布朗·詹姆斯",
    "follower_count": 321,
    "description": "著名篮球运动员",
    "country": "美国"
  },
  {
    "name": "YouTube",
    "follower_count": 654,
    "description": "视频分享网站",
    "country": "美国"
  },
  {
    "name": "埃隆·马斯克",
    "follower_count": 987,
    "description": "企业家和创新者",
    "country": "南非"
  },
  {
    "name": "Twitter",
    "follower_count": 234,
    "description": "微博客服务",
    "country": "美国"
  },
  {
    "name": "塞雷娜·威廉姆斯",
    "follower_count": 567,
    "description": "传奇网球运动员",
    "country": "美国"
  },
  {
    "name": "Snapchat",
    "follower_count": 890,
    "description": "消息应用",
    "country": "美国"
  },
  {
    "name": "内马尔·儒尼奥尔",
    "follower_count": 456,
    "description": "巴西足球明星",
    "country": "巴西"
  },
  {
    "name": "Google",
    "follower_count": 123,
    "description": "搜索引擎巨头",
    "country": "美国"
  },
  {
    "name": "泰勒·斯威夫特",
    "follower_count": 789,
    "description": "流行歌手兼词曲作者",
    "country": "美国"
  },
  {
    "name": "微软",
    "follower_count": 321,
    "description": "科技公司",
    "country": "美国"
  },
  {
    "name": "漫威",
    "follower_count": 654,
    "description": "流行漫画书和电影系列",
    "country": "美国"
  },
  {
    "name": "亚马逊",
    "follower_count": 987,
    "description": "在线零售商",
    "country": "美国"
  },
  {
    "name": "Netflix",
    "follower_count": 234,
    "description": "流媒体服务",
    "country": "美国"
  }
]
def aprints(a,b):

    print(f"选择A为{a["name"]},一个{a["description"]}，来自{a["country"]}")
    print("VS")
    print(f"选择b为{b["name"]},一个{b["description"]}，来自{b["country"]}")

def compare(a,b,c):
    f=[]
    if a["follower_count"]>b["follower_count"]:
        # print(f"a胜利了！{a["follower_count"]}")
        # print(b["follower_count"])
        # print(f"你输入的{c}")
        d="a"
    elif a["follower_count"]<b["follower_count"]:
        # print(f"b胜利了！{a["follower_count"]}")
        # print(b["follower_count"])
        # print(f"你输入的{c}")
        d="b"
    if c == "a" and d=="a" :
        f.append(a)
        # print(f)
        d="胜利"
        print("恭喜你猜对了！")
    elif c=="b"and d =="b":
        f.append(b)
        # print(f)
        d="胜利"
        print("恭喜你猜对了！")
    else:
        d="失败"
        print("对不起你失败了！")
        f=[[1]]
    return d,f

    

    #     d="胜利"
    #     print("恭喜您获得胜利！")
    #     c =
    #     return d
    # elif c != d:
    #     d="失败"
    #     print("对不起您失败了")
    #     return d

def Game(data):
    d = "胜利"
    e = 0
    datas=data
    a=datas[random.randint(0,len(datas)-1)]
    datas.remove(a)
    b=datas[random.randint(0,len(datas)-1)]
    datas.remove(b)
    while d == "胜利":
        if b in datas:
            datas.remove(b)
        aprints(a,b)
        userc=input("请选择 A or B:\n")
        os.system('cls')
        judgment=compare(a,b,userc)
        d = judgment[0]
        if d == "失败":
            break
            
        # d = compare(a,b,userc)[0]

        if d == "胜利":
            e+=1
            print(f"您一共获得{e}分")
        # print(judgment[1][0])
        if judgment[1][0]!=1:
            # print("原始字典",datas[random.randint(0,len(datas)-1)])
            # print("列表",judgment[1][0])
            # print("打印",a)
            a=judgment[1][0]
            # print("打印",a)
            if len(datas)>1:
                b=random.choice(datas)
            elif len(datas)==1:
                # print(datas)
                b=datas[0]
            else:
                d = "通关"
                print("恭喜你通关了！")
                return d
            
            
        
            
        
    
Game(data)
#创建datas1个列表，获取总字典


#用变量a获取随机字典并打印字典的键值对


#用变量b获取随机字典并打印字典的键值对

#获取用户输入选择a或者b

#比较两个字典的一个值，如果用户输入大于另外一个字典，结束游戏并打印游戏结束你输了！

#比较两个字典的一个值，如果用户输入大于另外一个字典，继续游戏（）

#总列表减去字典a和b

#更新变量a为列表字典的len长度的随机值








