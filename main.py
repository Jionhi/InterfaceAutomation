import requests

url = "https://httpbin.org/ip"
res = requests.get(url=url)
print(res.json())