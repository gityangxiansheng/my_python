
import pandas as pd
# hoom_linkes1 = ["https://item.jd.com/100047498366.html", "https://item.jd.com/100046247554.html"]
# linkes_df = pd.DataFrame(hoom_linkes1,columns=['链接'])
# linkes_df.to_csv(r'C:\Users\Administrator\Desktop\BaiduSyncdisk\爬虫学习\DrissionPage\京东.scv',index=False)
# link = pd.read_csv(r'C:\Users\Administrator\Desktop\BaiduSyncdisk\爬虫学习\DrissionPage\京东.scv')
# link_list = link["链接"].to_list()
# print(link_list)


datas = pd.read_csv(r'C:\Users\Administrator\Desktop\BaiduSyncdisk\爬虫学习\DrissionPage\京东_data copy.csv')

print(datas.iloc[-1, 0])