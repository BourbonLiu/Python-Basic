import requests, bs4

url = '../HTML/table.html'
htmlFile = open(url, encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')

mycountry = [] # 國名
myriver = []   # 河川
mystate = []   # 洲名

tableobj = objSoup.find('table').find('tbody')
tables = tableobj.find_all('tr')

for table in tables:
    allTd = table.find_all('td')
    country = allTd[1]                           # 國家節點
    mycountry.append(country.text)
    river = country.find_previous_sibling('td')  # 前一個節點，find_previous_sibling()回傳的是包含標籤的內容
    myriver.append(river.text)
    state = country.find_next_sibling('td')      # 下一個節點，find_next_sibling()回傳的是包含標籤的內容
    mystate.append(state.text)

print("國家 = ", mycountry)
print("河川 = ", myriver)
print("洲名 = ", mystate)
data1 = dict(zip(mycountry, myriver))
data2 = dict(zip(mystate, mycountry))
print(data1)
print(data2)