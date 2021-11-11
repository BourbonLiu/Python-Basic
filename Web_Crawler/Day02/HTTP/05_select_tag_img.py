import bs4

htmlFile = open('../HTML/myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
imgTag = objSoup.select('img')    # select會回傳一個list
print(len(imgTag))
print(imgTag)
print("--------------------------")
for img in imgTag:
    print(img)
    print(img.get('src'))
    print(img['src'])
    print("--------------------------")

