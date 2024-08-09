import requests 
from datetime import datetime  
from dateutil.relativedelta import relativedelta  

ArrCity = "HGH"

#抓取近三个月数据data为主要修改内容arrCity为ata机场代号month为月份
now = datetime.now()  
nows = now + relativedelta(months=1)  
formatted_now = nows.strftime("%m")
datav=[]
for s in range(3):
    nows = now + relativedelta(months=s) 
    formatted_now = nows.strftime("%m")
    print(formatted_now)
    url = "https://b2c.csair.com/portal/minPrice/queryMinPriceInMonth?type__1188=QqRxnDyDRDc7oGNDQiiQA8wxjx6ODBlOoD"
    headers={
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Cookie":"JSESSIONID=E34323AE10CBD409E1C5D894C3F1694C; language=zh_CN; sid=45da243e03ff468ebf56e24507f34edc; acw_tc=784e2c8817125540549985351e25e617ac7bc29592cd1a35e7b07a0de3bcdb; cookiesession1=678B286AA8CBF0FF78C8DF67D3EF0BA3; WT.al_flight=WT.al_hctype(S)%3AWT.al_adultnum(1)%3AWT.al_childnum(0)%3AWT.al_infantnum(0)%3AWT.al_orgcity1(CGO)%3AWT.al_dstcity1(HGH)%3AWT.al_orgdate1(2024-04-30); acw_sc__v2=66138047425f4ef518ee614054e9a29146477a03; _gscu_422057653=12554051fxst7751; _gscbrs_422057653=1; _gscs_422057653=12554051zzx0pw51|pv:1; _gcl_au=1.1.1691713225.1712554052; ssxmod_itna=Yq+xyDcGPQqx0Dl4iqozYqclhSGCK+/zeoDBwDo4iNDnD8x7YDv+GvD0r8Andy0oNQUeSrf5MbOleqeDjgnroT+DB3DEx0=K+KWPiinDCeDIDWeDiDG4=DFxYoDex5QDFbVzzZnwxWKDKx0kDY5DwgH8DYPDWxDFE20qNZDkNDDzNAENNQxDEmIC7rAsK4D1QY5xemKD9x0CDlP42FoD0od6NGvCEUfvvQIG440OD0F+0EphDB4kSr57zK2HvlaelmTeYm+qglx5QlWaqnTYilxqeahxQlxxNgn5HG=ZNDDWi7raeYD=; ssxmod_itna2=Yq+xyDcGPQqx0Dl4iqozYqclhSGCK+/zKD8uC40KqD/YIFDFhpiK+O4Dv9xg586D4APkqzZdYrsYe3LAjI9DzmA=athtoMaUrZRDonIdpP9fj6AqNZIyfN=S1kkBiNVn5hy+pw9UC/C57Ogqzi6H1lZHsRDAwdK5mp1m=iZA8b/YIzrFzUhIvYtHmqUFhEaf=+8uh9jPWI3O7ixnhS2yi/7dhctEI6BMIxyK6F932oxM2EfLRoLaRDhpXUW9z/8Cb8qnRNMCybyCkWLAXpV1k0UMBEMti=p6BzN10jTXQlBL/6phB5YUxC4DQIxYDqm4i/G5++tQGQQY4sh=FYlCB=7ipD4QKDqA2q8p3ID1jx5ZA3Dg=i0eD08Dij5YD===; tfstk=fipqDcmXxxHV3ARGza6NTvxmRc6AT93ISd_1jhxGcZbm61bwaFxtDn16jN8wPanGjqbMqU8y8rwO1ItGSaxTCmQ6GN8yPF-f1tX1QP8CycQfhEMw_ebJc19wXRSMjFnA5mhWDnBOI2gQQvtvDHJ2vhJNigflj32cSsm6AILdI2gIF2s4DcWM1-k6DT-lyGS0mNYgqgjAro4DSZfurMSdINYGI0zlbME0IOfMq8c5knxgUM1mlJXgKIDkrs7H4XegQ8j7RwtmQJwHUQ5N-v_zIRvP03ILmUeE1wAdl6_HrYwVQ3jwlaTnK8WlTBK1bEk4ntOkwKBXF2rdgF7ftL1zoSjF3Z5Hn_EULn5MaLWXnVFpV37cTTOSwq113ERdJsc-yF-PlFvVZru55BtWn_8nP88O_BK1bEk4nejy-PIoY4v9gPVNigIPR0ouMZEgmdjsbeFT6_Xd4wifc5FOigIPR0oz65Clyg7Ici1..",
        "Referer":"https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=CGO&c2=HGH&d1=2024-04-30&at=1&ct=0&it=0&b1=CGO&b2=HGH",
        "Sec-Fetch-Site":"same-origin",
        }
    data={'dep': "", 'arr': "", 'depCity': "CGO", 'arrCity': f"{ArrCity}", 'month': f"2024-{formatted_now}", 'channel': "B2CPC1"}
    datas = requests.post(url=url,headers=headers,json=data).json()
    for ss in datas["data"]:
        datav.append(ss)

# datav = [{'date': '2024-04-15', 'price': 400}, {'date': '2024-04-12', 'price': 340}]
sorted_datav = sorted(datav, key=lambda x: x['price'])
print(f"近三个月前往{ArrCity}的低价机票前三名分别是:\n"
      f"\t{sorted_datav[0]["date"]}\t价格为{sorted_datav[0]["price"]}元\n"
      f"\t{sorted_datav[1]["date"]}\t价格为{sorted_datav[1]["price"]}元\n"
      f"\t{sorted_datav[2]["date"]}\t价格为{sorted_datav[2]["price"]}元\n"
      )




