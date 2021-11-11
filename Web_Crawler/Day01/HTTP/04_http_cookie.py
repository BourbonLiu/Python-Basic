import requests

url = "http://httpbin.org/cookies"

cookies = dict(name='Aggie Tang')
r = requests.get(url, cookies=cookies)
print(r.text)
