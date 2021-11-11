import requests
from bs4 import BeautifulSoup

# 使用BeautifulSoup下載檔案
url = 'http://www.tenlong.com.tw'

try:
    htmlfile = requests.get(url)
    print("網頁下載成功")
except Exception as err:                                # err是系統自訂的錯誤訊息
    print("網頁下載失敗: %s" % err)

htmlfile.encoding = "utf-8"
soup = BeautifulSoup(htmlfile.text, "lxml")

fn = '../HTML/iter2.txt'
fp = open(fn, "w", encoding="utf8")
fp.write(soup.prettify())              # 透過prettify寫入的檔案排版會和原HTML一樣
print("下載網頁內容成功")
fp.close()