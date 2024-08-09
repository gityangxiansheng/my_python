import pandas as pd

# 创建一个示例 DataFrame

data = pd.read_excel(r"C:\Users\Administrator\Desktop\新建文件夹 (5)\新建文件夹 (6)\万滩镇工作开展情况日报表2024.3.8.xlsx")

# # 使用 iterrows() 方法遍历每一行
# for index, row in data.iterrows():
#     # 遍历每一行的每个单元格
#     for column in data.columns:
#         value = row[column]
#         if value == "司法所":
#             #获取行索引和列索引
#             row_index = index
#             column_index = data.columns.get_loc(column)+1
            
# data = {}           
#循环数据框的行和列
for index, row in data.iterrows():
    #循环列
    for column in data.columns:
        #获得循环的值
        value = row[column]
        #如果循环的值== "工作开展情况"
        if value == "工作开展情况":
            #获取当前行索引
            row_index = index
            print(row_index)
            #获取数字列名
            column_index = data.columns.get_loc(column)
            #获取str列名
            columns = data.columns[column_index]
            #从第一行开始循环工作开展情况列的内容
            for values in data[columns][1:]:
                #如果不是空的值，且长度大于10
                if type(values) == str and len(values) > 10:
                    # print(values)
                    
                    # print("\n")
                    数字列名 = data.columns.get_loc(column)-1
                    行索引 = data.columns.isin(["values"])
                    print(行索引)
                    # print(数字列名)
                    #获取values的行索引
                    # 行索引 = data.index.values
                    print(行索引)
                    # print(数字列名,"\n",行索引)
                    # print(data.iloc[行索引,数字列名])
                    # data[values]:
                    
            

            #遍历当前列的所有行，找到类型为str，and长度超过10的数据，储存行列坐标print(values)
            #列坐标-1找到站所名
            #将站所名作为键、内容作为值添加到字典中

#打开一个模板文件，遍历所有行和列，找到字典的第一个键，获得其坐标，将内容填充至列+1的位置
#输出为表格


            


        
#返回value的行索引和列索引