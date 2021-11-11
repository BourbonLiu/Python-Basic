from bs4 import BeautifulSoup

html_str = "<div id='msg' class='body'>Hello World! <p> Final Test <p></div>"
soup = BeautifulSoup(html_str, "lxml")
tag = soup.div


print(tag.name)
print(tag["id"])
print(tag["class"])       # 因為class可能有多個，所以返回的是list
print(tag.attrs)
print(soup)               # BeautifulSoup具有自動把標籤補齊的功能

print("-------------------------------------------------------------------")

print(tag.string)         # string可以剖析該標籤的網頁內容，但如果該標籤有子標籤則無法剖析
print(type(tag.string))
print(tag.text)           # text可以剖析該標籤和其子標籤的網頁內容
print(type(tag.text))

print("-------------------------------------------------------------------")

print(tag.get_text())    # get_text()一樣可以取得標籤內容，另外可輸入參數來分隔子標籤的內容
print(tag.get_text("-"))
print(tag.get_text("-", strip=True))

print("-------------------------------------------------------------------")

html_str = "<p><!-- 註解文字 --></p>"
soup = BeautifulSoup(html_str, "lxml")
comment = soup.p.string
print(comment)
print(type(comment))       # Comment(註解)型態