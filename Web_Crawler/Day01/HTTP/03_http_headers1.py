import requests

htmlfile = requests.get("https://www.lccnet.com.tw/lccnet")

# 取得Response的header
print(htmlfile.headers['Content-Type'])
print(htmlfile.headers['Content-Length'])
print(htmlfile.headers['Date'])
print(htmlfile.headers['Server'])