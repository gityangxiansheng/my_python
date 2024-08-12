import pandas as pd

data = pd.read_csv(r"C:\py4\BaiduSyncdisk\python\26day\nato_phonetic_alphabet.csv")
# print(data)

data_dijkse= {row.letter:row.code  for (index,row) in data.iterrows() }
# print(data_dijkse)
a=True
while a:
    int=input("请输入文本：").upper()
    data_list=[data_dijkse[ss] for ss in int]
    print(int)
    print(data_list)


# for (index,row) in data.iterrows():
#     print(row.letter,row.code)