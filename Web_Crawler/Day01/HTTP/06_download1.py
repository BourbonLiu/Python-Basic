import requests

# 沒有使用BeautifulSoup下載檔案
url = 'http://www.tenlong.com.tw'

try:
    htmlfile = requests.get(url)
    print("網頁下載成功")
except Exception as err:                                # err是系統自訂的錯誤訊息
    print("網頁下載失敗: %s" % err)

fn = '../HTML/iter1.txt'
with open(fn, 'wb', encoding="utf8") as fp:                              # 以二進位儲存
    for saveFile in htmlfile.iter_content(10240):
        size = fp.write(saveFile)
        print(size)                                     # 列出每次寫入大小
    print("下載HTML成功")

fp.close()