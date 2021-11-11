import requests

url = 'http://wwww.24ht.com.tw/'
htmlfile = requests.get(url)
htmlfile.raise_for_status()  # 406代表網頁伺服器阻擋



