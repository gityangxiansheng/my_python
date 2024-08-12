
# ssa = [1,2,3]
# new_ssa = [n*6    for n in ssa]
# print(new_ssa)


# name = "Angela"

# new_list = [s for s in name]
# print(new_list)

# name = []

# new_list = [s**2/10  for s in range(0,101)  if s % 2 == 0 ]
# print(new_list)


# name = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']

# names = [n.upper() for n in name if len(n) >= 5 ]
# print(names)


# numbers = [1,1,2,3,5,8,13,21,34,55]
# numberss=[]
# # for n in numbers:
# #     n = n**2
# #     numberss.append(n)
# # print(numberss)
# numberss=[n**2 for n in numbers  ]
# print(numberss)


# with open(r"C:\py4\BaiduSyncdisk\python\26day\1.txt") as one:
#     ones=one.readlines()
#     print(ones)
    # oness=ones.replace("\n","")
    # print(oness)

    # onesss=[s for s in ones  if ]
    # for s in ones:
    #     if s == """\"""" or s == "n" or s == "\n":
    #         pass
    #     else:
    #         print(s)
    # print(int(ones))
# with open(r"C:\py4\BaiduSyncdisk\python\26day\2.txt") as t:
#     ts=t.readlines()
#     print(ts)

# print(oness)
# print(tss)

# ccs = [int(num.replace("\n","")) for num in ts  if num in ones ]
# print(ccs)


import random

# name = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
# # students_scores = { new_key:new_value for student in names}
# students_scores = { s:random.randint(0,101) for s   in name}
# print(students_scores)

# pass_students = {key:value for (key,value) in students_scores.items() if value>=60}
# print(pass_students)

# data ="What is the Airspeed Velocity of an Unladen Swallow?"
# datas = {ss:len(ss) for ss in data.split()}
# print(datas)

# data = {"Monday":4,"uesday":5,"wednesday":15,"Thursday": 14}

# datas = {key:value * 9 / 5 + 32 for (key,value) in data.items() }
# print(datas)