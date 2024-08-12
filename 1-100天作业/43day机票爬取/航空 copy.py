import requests 
from datetime import datetime  
from dateutil.relativedelta import relativedelta  

url = "https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=python&city=101180100&experience=&payType=&partTime=&degree=&industry=&scale=&stage=&position=&jobType=&salary=&multiBusinessDistrict=&multiSubway=&page=1&pageSize=30"
headers={
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cookie':'wd_guid=4a4f8f31-1623-4f5e-a5e9-a2dcb318a1dd; historyState=state; __g=-; __l=l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3Dpython%26city%3D101180100&r=&g=&s=3&friend_source=0; _bl_uid=wml6yubwtveh9t721pw5k7sgqU2g; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1712733349; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1712733349; boss_login_mode=sms; wt2=DMGl-FZFpn_QsFDhig4bY8oVST5UhbK960jYDTdsUgfu81WwkNa_Y34bSwJKRfwr5QRS2PJ40EbCKbj3PMO491Q~~; wbg=0; zp_at=ca_JRix5oxiwKgpwEGmn0B1iIbyXU7CqILbUCaoBTtM~; collection_pop_window=1; __zp_stoken__=f19afw4Fzw74WR2QNfFsBYHhBUWpTU8KxeMOHf01LYmp2UVbCsMKzTWRyQ0nDhW7Cqk3Ck8OFwrVVwrpBxIdNwozCkcKWwpzEh07CkcSlw7jChMKlxLXCpMK8wpg%2BNxUODAEMFAMNAA0OFQwBDA0WFAkUFQ4MAQxEKMO%2BecKIQj47PyBAV0kNVFNZTmZACVNBSj5HDgsBC0cyPj8%2BO8OHwr7Csy7CsMK8wrovwrnCu8KwFj9GOzzCvy0tP3oKKQrDggkKIgrCu8OKXcOPWCEIw5%2FCscSwJj48wr%2FEsT4xEEU%2FQkc%2FPkZCMSAxwr7DnMOMWDUSw6LCs0QuPiI5Pz5ERDE%2FPkJCRyM%2BRjovPz8uPhcPFg8VLjjCs0%2FCu8OQPz4%3D; __c=1712733348; __a=68866487.1712733348..1712733348.6.1.6.6; geek_zp_token=V1R9gjE-H72l5oVtRuzh8fKii56jjWwCQ~',
    'Referer':'https://www.zhipin.com/web/geek/job?query=python&city=101180100',
    'Sec-Fetch-Site':'same-origin',
}
datas = requests.get(url=url,headers=headers).json()

print(datas)
    






