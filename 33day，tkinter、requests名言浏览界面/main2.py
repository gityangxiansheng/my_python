import requests 

requestsss = requests.get(url="https://the-trivia-api.com/api/questions?limit=9&difficulty=easy")
requestsss.raise_for_status()
data = requestsss.json()


print(data)