import requests, bs4

url = '../HTML/table.html'
htmlFile = open(url, encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')

tableobj = objSoup.find('table').find('tbody')
tables = tableobj.find_all('tr')    # 取得每一列
river = tables[1].find('td')        # 取得第二列的第一個元素
print(river.text)

print("----------------------------------------------------------------")

river_parent = river.parent()       # 取得父節點的資料，parent()回傳的是list
print(river_parent)

print("----------------------------------------------------------------")

river_parent = river.parent       # 取得父節點的資料，parent回傳的是tag
print(river_parent)

print("----------------------------------------------------------------")

river = tables[1].find_all('td')    # find_all回傳的是list
print(river)


