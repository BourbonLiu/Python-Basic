import requests, bs4

# 取得中國時報熱門新聞
url = 'https://www.chinatimes.com/world/?chdtv'
newshtml = requests.get(url)
objSoup = bs4.BeautifulSoup(newshtml.text, 'lxml')
itemobj = objSoup.find('section', class_ = 'hot-news')
itemobj = itemobj.find('ol', class_ = 'vertical-list')
items = itemobj.find_all('li')
for item in items:
    txt = item.h4.text
    print(txt)