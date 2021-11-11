import bs4

# 透過open開啟電腦的HTML檔
htmlFile = open('..\HTML\HTML_11.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')                  # open來的html檔不用加上text就能被BeautifulSoup解析
print("物件資料型態  = ", type(objSoup))
print("物件類型  = ", type(objSoup.title))
print("列印title = ", objSoup.title)
print("title內容 = ", objSoup.title.text)
