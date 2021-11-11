from selenium import webdriver
import os

driverPath = r'D:\LabCode\Python\chromedriver.exe'
url = r'D:\LabCode\Python\Web_Crawler\Day04\HTML\form.html'

driver = webdriver.Chrome(driverPath)
driver.implicitly_wait(10)
driver.get(url)


form1 = driver.find_element_by_xpath("/html/body/form[1]")
print(form1.text)
form2 = driver.find_element_by_xpath("//form[1]")
print(form2.tag_name)
form3 = driver.find_element_by_xpath("//form[@id='loginForm']")
print(form3.tag_name)

print("------------------------------------")

pwd1 = driver.find_element_by_xpath("//form/input[2][@name='password']")
print(pwd1.get_attribute("type"))
pwd2 = driver.find_element_by_xpath("//form[@id='loginForm']/input[2]")
print(pwd2.get_attribute("name"))
pwd3 = driver.find_element_by_xpath("//input[@name='continue']")
print(pwd3.get_attribute("value"))

print("------------------------------------")

clear1 = driver.find_element_by_xpath("//input[@name='continue'][@type='submit']")
print(clear1.get_attribute("type"))
clear2 = driver.find_element_by_xpath("//form[@id='loginForm']/input[4]")
print(clear2.get_attribute("type"))
clear3 = driver.find_element_by_xpath("/html/body/a[2]")
print(clear3.get_attribute("href"))

driver.quit()