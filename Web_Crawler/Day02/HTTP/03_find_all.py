import bs4
from bs4 import BeautifulSoup


with open("../HTML/Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")

tag_div = soup.find("div", id="q2")

tag_list = tag_div.find_all(["p", "span"])               # 找出所有<p>和<span>標籤
print(type(tag_list))                                    # 透過find_all()以name,class,id當參數，找到的資料是以tag組成的Resultset
print(tag_list)
print(tag_list[0].getText())

tag_list = tag_div.find_all(class_=["question", "selected"])  # 找出所有class是question和selected
print(tag_list)

print("---------------------------------------------")

# 找出所有標籤清單
tag_list = tag_div.find_all(True)
print(tag_list)

print("---------------------------------------------")

# find_all()以text當參數，找到的資料是NavigableString組成的Resultset
nStr_list = tag_div.find_all(text=True)
print(nStr_list)

nStr_list = tag_div.find_all(text=["0", "40"])
print(nStr_list)

print("---------------------------------------------")

# 如果資料量很多比可以透過limit來限制資料筆數
tag_list = soup.find_all("p", class_="question", limit=2)
print(tag_list)

for question in tag_list:
    print(question.a.string)
