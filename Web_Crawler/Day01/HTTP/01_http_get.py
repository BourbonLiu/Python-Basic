import requests

url = 'https://www.lccnet.com.tw/lccnet'
htmlfile = requests.get(url)
print(htmlfile)
print(type(htmlfile))         # Response
print(htmlfile.status_code)