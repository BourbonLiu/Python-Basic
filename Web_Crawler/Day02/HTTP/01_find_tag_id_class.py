import bs4

with open("../HTML/Example.html", "r", encoding="utf8") as fp:
    soup = bs4.BeautifulSoup(fp, "lxml")

# 使用find只會找到"第一個"符合條件的內容
tag_li = soup.find(attrs={"class": "response"})  # 透過attrs輸入標籤內的屬性
tag_span = tag_li.find("span")
print(type(tag_span))                            # find找到的資料型態是Tag
print(tag_span.string)

print("--------------------------------------------------")

tag_div = soup.find(id="q2")               # 透過id尋找
tag_li = tag_div.find(class_="response")   # 透過class尋找
tag_span = tag_li.find("span")             # 透過tag尋找
print(tag_span.string)

print("--------------------------------------------------")

for element in tag_div:
    if type(element) is bs4.element.Tag:
        print(element.text)

print("--------------------------------------------------")

# 透過標籤尋找內容
tag_p = soup.find(name="p")                # 透過tag尋找，name可以省略
print(tag_p.a.string)
tag_a = tag_p.find(name="a")
print(tag_a.string)

print("--------------------------------------------------")

tag_div = soup.find("div", class_="question")  # 尋找標籤是div並且class=question的內容
print(type(tag_div.text))                      # 是string
print(tag_div.text)

tag_p = soup.find("p", class_="question")
print(type(tag_p.string))                      # 是NavigableString
print(tag_p.string)

print("--------------------------------------------------")

nStr = soup.find(text="請問你的性別?")          # 使用text來尋找
print(nStr)
nStr = soup.find(text="10")
print(nStr)
nStr = soup.find(text="男-")
print(nStr)

print(type(nStr))        # NavigableString型態
print(nStr.parent.name)  # 父標籤名稱