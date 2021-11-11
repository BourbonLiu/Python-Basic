import re
from bs4 import BeautifulSoup

with open("../HTML/Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
# 使用正規運算式搜尋文字內容
pattern = re.compile("男-")
nStr = soup.find(text=pattern)
print(nStr)

print("---------------------")

pattern = re.compile("\w+-")
nStr_list = soup.find_all(text=pattern)
print(nStr_list)

