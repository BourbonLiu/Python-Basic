import re
from bs4 import BeautifulSoup

with open("../HTML/Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")

pattern = re.compile("\w+@\w+\.\w+")

nStr_list = soup.find_all(text=pattern)          # 這裡find_all()找到的是以NavigableString組成的ResultSet

for email in nStr_list:
    print(email.strip())                        # strip()會把資料從NavigableString轉成string

print("---------------------")

str_list = pattern.findall(soup.text)           # 這裡一定要是soup.text，不可以是soup
print(str_list)


print("---------------------")

pattern = "\w+@\w+\.\w+"
str_list = re.findall(pattern, soup.text)
print(str_list)

