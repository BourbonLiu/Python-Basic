import requests, bs4

url = '../HTML/table.html'
htmlFile = open(url, encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')

myriver = []  # 河川
tableobj = objSoup.find('table').find('tbody')
tables = tableobj.find_all('tr')
for table in tables:
    river = table.find('td')           # 透過find剛好可以取得第一個td
    myriver.append(river.text)

mycountry = []  # 國家
for table in tables:
    allTd = table.find_all('td')  # 透過find無法取得第二個td,所以使用find_all取
    country = allTd[1]
    mycountry.append(country.text)

print("國家 = ", mycountry)
print("河川 = ", myriver)
data = dict(zip(mycountry, myriver))  # 把mycountry和myriver合併成字典
print(data)  # 字典顯示結果
