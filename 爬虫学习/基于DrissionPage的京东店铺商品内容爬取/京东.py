from DrissionPage import WebPage
from DrissionPage import ChromiumPage
from DrissionPage import ChromiumPage, ChromiumOptions
from DrissionPage.common import Keys
import pandas as pd
from DrissionPage.errors import *
from DataRecorder import Recorder
from concurrent.futures import ThreadPoolExecutor  
from pandas.errors import EmptyDataError
from DrissionPage.common import Settings
##登陆操作
#打开网页
#人工登录
#进入主页等待

def book_page():
    """返回一个page属性的列表,页码的链接"""
    pahe_link = page.eles('x://div[@class="jPage"]/a/@href')[:-1]
    pahe_links = [_.link for _ in pahe_link ]
    return pahe_links

def hoom(page_links):
    """传入一个pagelink，返回一个字典，并保存一个json文件"""
    #  获取第一页的所有商品链接储存至字典
    hoom_linkes1s = page.eles('x://div[@class="j-module"]/ul/li/div/div[3]/div[1]/a/@href')
    hoom_linkes1 = [_.link for _ in hoom_linkes1s]
    c = 1
    ##获取2至-1的页的所有商品储存至字典
    #循环2页到最后一页
    for page_link in page_links:
        print(page_link)
        #新建页打开链接
        new_page = page.new_tab(page_link)
        # print(hoom_dict)
        #获取商品数据并储存至字典
        c+=1
        hoom_linkess = new_page.eles('x://div[@class="j-module"]/ul/li/div/div[3]/div[1]/a/@href')
        for link in hoom_linkess:
            hoom_linkes1.append(link.link)
        new_page.close()
    print("共获取到链接:",len(hoom_linkes1),"个,已储存至京东_link.csv")
    linkes_df = pd.DataFrame(hoom_linkes1,columns=['链接'])
    linkes_df.to_csv(r'C:\Users\Administrator\Desktop\BaiduSyncdisk\爬虫学习\DrissionPage\京东_link.csv',index=False)    
    return hoom_linkes1


def clck(link):
    global indx
    #打开新的标签页
    new = page.new_tab(link)
    new.wait(2,3)
    try:
        new.ele('x://div[@class="verifyBtn"]')
        input("请进行人工验证！")
    except ElementNotFoundError:
    # 判断元素是否存在，如果存在就获取配置列表依次点击
        try:
            new.ele('x://div[@id="choose-attr-1"]')
            #获取颜色元素定位
            colo = new.eles(f'x://div[@id="choose-attr-1"]/div[2]/div/a[1]')
            #获取配置元素定位
            configurations = new.eles(f'x://div[@id="choose-attr-2"]/div[2]/div/a[1]')
            #点击一下第二个配置，然后等待
            colo[1].click()
            new.wait(2,4)
            ##循环等待点击配置
            for _ in range(len(configurations)):
                configurations = new.eles(f'x://div[@id="choose-attr-2"]/div[2]/div/a[1]')
                configurations[_].click()
                new.wait(3,6)
                tlitle = str(new.eles(f'x://div[@id="choose-attr-1"]/div[2]/div[1]/@title')[0])
                if "无此商品" in tlitle:
                    colo = new.eles(f'x://div[@id="choose-attr-1"]/div[2]/div/a[1]')
                    configurations = new.eles(f'x://div[@id="choose-attr-2"]/div[2]/div/a[1]')
                    print(f"无此商品{configurations[_]}")
                    colo[-1].click()
                    new.wait(3,4)
                pay = new.ele(f'x://span[@class="p-price"]/span[2]').text 
                configurations = new.eles(f'x://div[@id="choose-attr-2"]/div[2]/div/a[1]')
                try:
                    coupon = new.ele('x://div[@id="summary-quan"]//span[@class="text"]').text
                except ElementNotFoundError:
                    coupon = ("暂无优惠")
                else:
                    coupon = new.ele('x://div[@id="summary-quan"]//span[@class="text"]').text
                r.add_data([str(indx),str(new.ele('x://div[@class="sku-name"]').text),str(configurations[_]).split("-")[1][:-2],str(link),str(coupon),str(pay)])
                r.record()
                indx += 1
        except ElementNotFoundError:
                try:
                    coupon = new.ele('x://div[@id="summary-quan"]//span[@class="text"]').text
                except ElementNotFoundError:
                    coupon = ("暂无优惠")
                else:
                    coupon = new.ele('x://div[@id="summary-quan"]//span[@class="text"]').text
                pay = new.ele(f'x://span[@class="p-price"]/span[2]').text 
                #添加行
                r.add_data([str(indx),str(new.ele('x://div[@class="sku-name"]').text),str(0),str(link),str(coupon),str(pay)])
                r.record()
                indx += 1
                print(coupon)
                print(f"当前配置是{new.ele('x://div[@class="sku-name"]').text}规格是：空，优惠：{coupon}，价格是：{pay}")
    new.close()

       
#建立一个实例   
page = ChromiumPage()
path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
co = ChromiumOptions().set_browser_path(path)
page = ChromiumPage(co)
page.get('https://www.baidu.com')        
page.get('https://mall.jd.com/view_search-466323-8345047-0-1-24-1.html')
input()
Settings.raise_when_ele_not_found = True
#如果字典是空的就运行函数重新获取链接，不空就读取链接到列表。
try:
    links = pd.read_csv(r'C:\Users\Administrator\Desktop\BaiduSyncdisk\爬虫学习\DrissionPage\京东_link.csv')
    link_list = links["链接"].to_list()
except EmptyDataError :
    page_links = book_page()
    link_list =hoom(page_links)
    

# 打开文件如果序号存在，捕获序号，如果序号不存在序号返回0
try:
    datas = pd.read_csv(r'C:\Users\Administrator\Desktop\BaiduSyncdisk\爬虫学习\DrissionPage\京东_data.csv')
    indx = datas.iloc[-1, 0]
except EmptyDataError :
    indx = 0    

#新建一个多线程写入数据    
r = Recorder(r'C:\Users\Administrator\Desktop\BaiduSyncdisk\爬虫学习\DrissionPage\京东_data.csv')

#多并发爬取详情页
with ThreadPoolExecutor(max_workers=6) as executor:  
    # 使用map函数并行地应用detail_tab函数到detail_links_all列表的每个元素  
    results = list(executor.map(clck, link_list[int(indx):]))  
    executor.shutdown(wait=True)

