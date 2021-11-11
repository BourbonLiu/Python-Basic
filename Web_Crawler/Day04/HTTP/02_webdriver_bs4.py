from selenium import webdriver
from bs4 import BeautifulSoup

driverPath = r'D:\LabCode\Python\chromedriver.exe'
url = "https://www.lccnet.com.tw/lccnet"

driver = webdriver.Chrome(executable_path=driverPath)
driver.implicitly_wait(10)
driver.get(url)


soup = BeautifulSoup(driver.page_source, "lxml")

tag_h1 = soup.find("h2")
print(tag_h1.text)

tag_p = soup.find("p")
print(tag_p.text)

print("--------------------------------------------------")

fp = open("../HTML/lccnet.html", "w", encoding="utf8")
fp.write(soup.prettify())
print("下載HTML檔完成")


fp.close()
driver.quit()