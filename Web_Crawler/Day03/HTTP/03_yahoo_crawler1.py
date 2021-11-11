import requests, bs4

# 爬yahoo本週新片
url = 'https://movies.yahoo.com.tw/movie_thisweek.html'
moviehtml = requests.get(url)
objSoup = bs4.BeautifulSoup(moviehtml.text, 'lxml')

movieNum = 0
items = objSoup.find_all('div', 'release_info')
for item in items:
    movieNum += 1
    cName = item.find('div', 'release_movie_name').a.text.strip()
    eName = item.find('div', 'en').a.text.strip()
    rtime = item.find("div", class_ = "release_movie_time").text
    video = item.find('div','release_btn color_btnbox').find_all('a')[1]
    if 'href' in video.attrs:                               # 檢查預告片是否存在
        video = video['href']
    else:
        video = ''

    print('新片編號 : ', movieNum)
    print('中文片名 : ', cName)
    print('英文片名 : ', eName)
    print(rtime)
    print("預告片  : ",video)
    print("="*100)
