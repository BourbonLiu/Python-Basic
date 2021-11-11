import requests

url = 'https://www.lccnet.com.tw/lccnet'
htmlfile = requests.get(url)
if htmlfile.status_code == 200:
    print("取得網頁內容成功")
    print(htmlfile.text)  # 列印網頁內容
else:
    print("取得網頁內容失敗")
