import requests
import json


def hqshuj():
    url = 'https://www.alphavantage.co/query'
    parameters = {
        "function":"",
        "symbol":"",
        "interval":"",
        "apikey":""
    }
    r = requests.get(url,parameters)
    r_data = r.json()
    with open (r"python\36day\main.json","w") as rs:
        json.dump(r_data,rs)
        
hqshuj()
