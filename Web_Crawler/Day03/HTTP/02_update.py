from bs4 import BeautifulSoup
from bs4.element import NavigableString

soup = BeautifulSoup("<div><p>這是一段測試</p></div>", "lxml")
tag = soup.p
print(tag)

print("----------------------------------------")

new_tag = soup.new_tag("span")
new_tag.string = "Two"
tag.insert_before(new_tag)
print(soup.div)

new_string = soup.new_string("Three")
tag.insert_after(new_string)
print(soup.div)

tag.clear()
print(soup.div)

print("----------------------------------------")

tag.append("Allen")
print(soup.div)

new_string = NavigableString(" Liu")
tag.append(new_string)
print(soup.div)

new_tag = soup.new_tag("a", href="http://www.example.com")
tag.append(new_tag)
print(soup.div)

print("----------------------------------------")

new_tag = soup.new_tag("table")
new_tag.string = "這是表格"
soup.div.span.replace_with(new_tag)
print(soup.div)

print("----------------------------------------")

tag = soup.table
tag.name = "span"
tag["id"] = "s1"
tag["class"] = "css1"
tag.string = "新的標籤"
print(soup.div)

del tag["class"]
print(soup.div)
