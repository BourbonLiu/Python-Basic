import requests

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
# client端表頭資訊可以透過這個網站取得 http://httpbin.org/user-agent
# 也可以在瀏覽器開發人員工具取得

url = 'https://www.kingstone.com.tw/basic/2018730513521?zone=book&lid=book_index_reserve'

# htmlfile = requests.get(url)   # 如果沒有給表頭資訊有可能會被server端阻擋
htmlfile = requests.get(url, headers=headers)
htmlfile.raise_for_status()
print("偽裝瀏覽器擷取網路資料成功")
print(htmlfile.text)  # 列印網頁內容
