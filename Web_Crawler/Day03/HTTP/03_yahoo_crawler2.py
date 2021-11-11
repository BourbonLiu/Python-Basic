import requests, bs4

# 爬yahoo本週票房排行
url = 'https://movies.yahoo.com.tw/chart.html'
moviehtml = requests.get(url)
objSoup = bs4.BeautifulSoup(moviehtml.text, 'lxml')

itemsobj = objSoup.find('ul', 'ranking_list_r')
items = itemsobj.find_all('li')
print("台北本週票房排行榜\n")
for item in items:
    name = item.span.text
    rank = item.find('div', 'num').text
    print('片名 : ', name)
    print('名次 : ', rank)
    print()