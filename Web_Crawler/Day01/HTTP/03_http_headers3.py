import requests

url = "http://httpbin.org/user-agent"

r = requests.get(url)      # 沒有給header所以server端知道是從python發出的請求
print(r.text)

print("----------------------")

url_headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
r = requests.get(url, headers=url_headers)    # 給上header後server端會判定為是browser發出的請求
print(r.text)
