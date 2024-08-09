import pandas as pd

# f =  pd.DataFrame(r"c:\Users\Administrator\Desktop\ssa.xlsx")
# c:\Users\Administrator\Desktop\ssa.xlsx

data = pd.read_excel(r"C:\Users\Administrator\Desktop\新建文件夹 (5)\新建文件夹 (6)\万滩镇工作开展情况日报表2024.3.8.xlsx",header=2)

# print(data.iloc[0,0])



# print(df.loc["站所名称", 3])
# print( df.columns.get_loc(key="站所名称"))
# df.loc[0, 0]="112345646464564545564456431313"
# df.to_excel(r"c:\Users\Administrator\Desktop\万滩镇工作开展情况日报表2024.3.8.xlsx",index=False, header=False)


# cells = []
# coordinate = []
# for cell in df.iloc[:,1]:
#     cells.append(cell)
# df.columns.get_loc(cell)
# print(cells)
# #查找列名""并逐行填充cells列表
