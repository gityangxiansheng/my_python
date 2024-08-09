# def make_pie(index):
    
#     fruit=["苹果","李子","橙子"]
    
#     try:
#         fruits=fruit[index]
#     except IndexError :
#         print("水果派")
#     else:
#         print(fruits+"派")



# make_pie(4) 




facebook = [
    {"喜欢":21,"评论":2},
    {"喜欢":13,"评论":2,"转发":1},
    {"喜欢":33,"评论":8,"转发":3},
    {"评论":4,"转发":2},
    {"评论":1,"转发":1},
    {"喜欢":19,"评论":3},
]


total_likes = 0

for post in facebook:
    print(post)
    try:
        total_likes = total_likes + post["喜欢"]
    except:
        pass
    
    
print(total_likes)