import bs4, requests, os

url = 'https://www.lccnet.com.tw/lccnet'
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

html = requests.get(url, headers=headers)
html.raise_for_status()                             # 驗證網頁是否下載成功
print("網頁下載完成")

objSoup = bs4.BeautifulSoup(html.text, 'lxml')

imgTags = objSoup.select('img')
print("搜尋到的圖片數量 = ", len(imgTags))


dir = '../Images'                                   # 設定未來儲存圖片的資料夾
if os.path.exists(dir) == False:
    os.mkdir(dir)                                   # 建立資料夾供未來儲存圖片


if len(imgTags) > 0:
    for i in range(len(imgTags)):
        imgUrl = imgTags[i].get('src')               # 取得圖片的路徑
        print("%s 取得圖片路徑 " % imgUrl)
        finUrl = url + imgUrl                       # 取得圖片在Internet上的路徑
        print("%s 取得圖片網址 " % finUrl)
        picture = requests.get(finUrl)              # 下載圖片
        picture.raise_for_status()
        print("%s 圖片下載成功" % finUrl)

        # 先開啟檔案, 再儲存圖片
        # pictFile = open(os.path.join(dir, str(i)+'.img', 'wb')
        pictFile = open(os.path.join(dir, os.path.basename(imgUrl)), 'wb')   # wb:以binary寫入檔案
        for diskStorage in picture.iter_content(10240):  # 每10Kb為單位寫入
            pictFile.write(diskStorage)
        pictFile.close()                            # 關閉檔案
