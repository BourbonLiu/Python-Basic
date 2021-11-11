import requests
from bs4 import BeautifulSoup

# 取得工商時報熱門新聞
url = "https://www.chinatimes.com/newspapers/2602?chdtv"
html = requests.get(url)
soup = BeautifulSoup(html.text, "lxml")
rs = soup.find("section", class_ = "hot-news")
print(rs.h4.text,":")
rs = rs.find("ol").find_all("li")

for li in rs:
    rs2 = li.h4.text
    print(rs2)