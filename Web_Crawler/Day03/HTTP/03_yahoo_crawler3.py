import requests, bs4, os

url = 'https://movies.yahoo.com.tw/movie_thisweek.html'
moviehtml = requests.get(url)
objSoup = bs4.BeautifulSoup(moviehtml.text, 'lxml')

photos = []                                             # 放置劇照串列
items = objSoup.find_all('div', 'release_foto')
for item in items:
    photo = item.a.img['src']
    photos.append(photo)

print("搜尋到的圖片數量 = ", len(photos))                  # 列出搜尋到的圖片數量

dir = '../Images'
if os.path.exists(dir) == False:
    os.mkdir(dir)

for photo in photos:
    picture = requests.get(photo)
    picture.raise_for_status()

# 先開啟檔案, 再儲存圖片
    pictFile = open(os.path.join(dir, os.path.basename(photo)), 'wb')
    for diskStorage in picture.iter_content(10240):
        pictFile.write(diskStorage)
    print("%s 圖片下載成功" % photo)
    pictFile.close()                                    # 關閉檔案
