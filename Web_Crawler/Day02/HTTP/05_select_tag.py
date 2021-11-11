import bs4

htmlFile = open('../HTML/myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
pObjTag = objSoup.select('p')    # 透過tag去select
print(len(pObjTag))
print(pObjTag)
print("-------------------------")
for pObj in pObjTag:
    print(str(pObj))              # 是string，有標籤
    print(pObj.text)              # 是string，沒標籤
    print("-------------------------")

pObjTag = objSoup.select(".abc")  # 透過class去select
print(pObjTag)
