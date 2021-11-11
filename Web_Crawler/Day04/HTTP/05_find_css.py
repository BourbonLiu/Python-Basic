from selenium import webdriver
import os

from selenium.common.exceptions import NoSuchElementException

driverPath = r'D:\LabCode\Python\chromedriver.exe'
url = r'D:\LabCode\Python\Web_Crawler\Day04\HTML\form.html'

driver = webdriver.Chrome(driverPath)
driver.implicitly_wait(10)
driver.get(url)

p = driver.find_element_by_css_selector("p")
print(p.text)

id = driver.find_element_by_css_selector("#loginForm")
print(id.text)

cls = driver.find_element_by_css_selector(".question")
print(cls.text)


content = driver.find_element_by_css_selector("h3.content")
print(content.text)


driver.quit()