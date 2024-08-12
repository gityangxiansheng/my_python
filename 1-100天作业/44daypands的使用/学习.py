import pandas as pd
import numpy as np


#创建一个数据框架（（（（
data={"grammer":["Python","C","Java","G0",np.nan, "SQL","PHP","Python"],
"score":[1,2,np.nan,4,5,6,7,10]}
df = pd.DataFrame(data)
print(df)
#创建一个数据框架））））

#查找某个列中的某个数据所在的行（（（
python =df[df["grammer"] == "Python"]
print(python)
#查找某个列中的某个数据所在的行）））

#打印列名（（（
print(df.columns)
#打印列名）））
#修改列名（（（
df.rename(columns={"grammer":"a"},inplace=True)
print(df.columns)
#修改列名）））

#统计某列中出现的次数（（（

print(df["a"].value_counts())
#统计某列中出现的次数）））