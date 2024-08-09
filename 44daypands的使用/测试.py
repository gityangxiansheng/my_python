import pandas as pd
import numpy
 
ss = pd.read_excel(r"C:\Users\Administrator\Desktop\1.xlsx")
# print(ss)
# print(ss.loc[0])
# print(ss.dtypes)
# print(ss.columns)
# print(ss.index)
# print(ss[["a1","b1"]])
print(ss.loc[0:3])