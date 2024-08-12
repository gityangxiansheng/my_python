import requests  
import json  
  
def main():  
    ID = ""  
    urls = "https://aip.baidubce.com/rpc/2.0/nlp/v1/txt_monet"  
    access_token = 
  
    url = f"{urls}?"  
  
    payload = {
    "content_list":[
        {
            "content":"我今天跑步三公里",
            "query_list":[
                {
                    "query":"运动类型"
                },
                {
                    "query":"耗费时间"
                },
            ]
        },
        {
            "content":"我今天跑步三公里",
            "query_list":[
                {
                    "query":"运动类型"
                },
                {
                    "query":"耗费时间"
                },
            ]
        }
    ]
}
  
    # 发送POST请求，传入headers和json参数（requests库会自动将dict转换为JSON格式）  
    response = requests.post(url, json=payload)  # 使用json参数而不是data  
  
    # 检查响应状态码，并打印响应内容  
    if response.status_code == 200:  
        print("请求成功，提取的关键词:")  
        result = response.json()  # 解析JSON响应
        print(result)
        print(json.dumps(result, ensure_ascii=False, indent=4))  # 格式化打印，确保中文正常显示  
    else:  
        print(f"请求失败，状态码：{response.status_code}")  
        print(response.text)  # 打印原始响应内容以便调试  
        print(f"错误详情：{response.json().get('error_msg', '未知错误')}")  # 尝试获取错误信息  
  
if __name__ == '__main__':  
    main()
    
    

