from selenium import webdriver
import os

driverPath = r'D:\LabCode\Python\chromedriver.exe'
url = r'D:\LabCode\Python\Web_Crawler\Day04\HTML\form.html'

driver = webdriver.Chrome(driverPath)
driver.implicitly_wait(10)
driver.get(url)


h3 = driver.find_element_by_tag_name("h3")                  # 透過標籤去尋找
print(h3.text)

form = driver.find_element_by_id("loginForm")               # 透過id去尋找
print(form.text)

content = driver.find_element_by_class_name("content")      # 透過class去尋找
print(content.text)

print("------------------------------------")

link1 = driver.find_element_by_link_text('Continue')         # 透過內容去尋找
print(link1.text)
link2 = driver.find_element_by_partial_link_text('Conti')    # 透過部分內容去尋找
print(link2.text)
link3 = driver.find_element_by_link_text('取消')
print(link3.text)
link4 = driver.find_element_by_partial_link_text('取')
print(link4.text)

print("------------------------------------")

user = driver.find_element_by_name("username")      # 透過name屬性去尋找
print(user.tag_name)
print(user.get_attribute("type"))

eles = driver.find_elements_by_name("continue")    # find_elements回傳的是list
for ele in eles:
    print(ele.get_attribute("type"))

driver.quit()