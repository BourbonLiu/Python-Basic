import requests, bs4
htmlFile = requests.get('http://www.tenlong.com.tw')
htmlFile.encoding = "utf8"
objSoup = bs4.BeautifulSoup(htmlFile.text, 'lxml')  # lxml為解析器，可以將Response轉成XML樹狀圖
                                                    # requests.get()來的response一定要.text才能經過BeautifulSoup解析


print(len(htmlFile.text))
# print(objSoup)
print("物件資料型態 ", type(objSoup))
print("物件類型  = ", type(objSoup.title))
print("列印title = ", objSoup.title)       # 連同title標籤和標籤裡的內容一起印出來
print("title內容 = ", objSoup.title.text)  # 只印出title標籤的內容

