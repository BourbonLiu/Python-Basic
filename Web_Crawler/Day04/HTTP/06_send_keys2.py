from selenium import webdriver

driverPath = r'D:\LabCode\Python\chromedriver.exe'
url = "https://www.google.com"

driver = webdriver.Chrome(driverPath)
driver.implicitly_wait(10)
driver.get(url)

keyword = driver.find_element_by_css_selector("body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
keyword.send_keys("新北市")
button = driver.find_element_by_css_selector("body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b")
button.click()

items = driver.find_elements_by_xpath('//*[@id="rso"]')

for item in items:
    h3 = item.find_element_by_tag_name("h3")
    print(h3.text)
    a = item.find_element_by_tag_name("a")
    print(a.get_attribute("href"))

button2 = driver.find_element_by_css_selector("#rso > div:nth-child(1) > div > div > div.tF2Cxc > div.yuRUbf > a")
button2.click()

