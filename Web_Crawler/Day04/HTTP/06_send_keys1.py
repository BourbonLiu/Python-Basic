from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driverPath = r'D:\LabCode\Python\chromedriver.exe'
url = "https://www.google.com"

driver = webdriver.Chrome(driverPath)
driver.implicitly_wait(10)
driver.get(url)

keyword = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
keyword.send_keys("新北市")
keyword.send_keys(Keys.ENTER)


items = driver.find_elements_by_xpath('//*[@id="rso"]')

for item in items:
    h3 = item.find_element_by_tag_name("h3")
    print(h3.text)
    a = item.find_element_by_tag_name("a")
    print(a.get_attribute("href"))
