import bs4

htmlFile = open('../HTML/myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
objTag = objSoup.select('#author')        # 透過id去select

print(len(objTag))

print(type(objTag))          # 透過select找到的資料型態是ResultSet
print(objTag)                # 印出一個list

print("-----------------------------------")

print(type(objTag[0]))       # Tag
print(objTag[0])

print("-----------------------------------")

print(type(str(objTag[0])))  # string，把tag轉成string
print(str(objTag[0]))
print(objTag[0].attrs)       # 取得該元素的所有屬性

print("-----------------------------------")
print(type(objTag[0].getText()))
print(objTag[0].getText())

print(type(objTag[0].string))
print(objTag[0].string)

print(type(objTag[0].text))
print(objTag[0].text)




