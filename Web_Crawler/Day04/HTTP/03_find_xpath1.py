from selenium import webdriver

driverPath = r'D:\LabCode\Python\chromedriver.exe'
url = r'D:\LabCode\Python\Web_Crawler\Day04\HTML\xPath_1.html'

browser = webdriver.Chrome(executable_path=driverPath)
browser.get(url)

n1 = browser.find_element_by_xpath('//h4')
print(n1.text)
n2 = browser.find_element_by_xpath('//body/section/h4')
print(n2.text)
n3 = browser.find_element_by_xpath('//section/h4')
print(n3.text)
n4 = browser.find_element_by_xpath('//body/*/h4')
print(n4.text)

print("-------------------------------------------------")

n1 = browser.find_element_by_xpath('//p')
print(n1.text)

print("-------------------------------------------------")

n1 = browser.find_element_by_xpath("//section/p[1]")
print(n1.text)
n2 = browser.find_element_by_xpath("//section/p[2]")
print(n2.text)

print("-------------------------------------------------")

pict = browser.find_element_by_xpath("//section/img")
print(pict.get_attribute('src'))

browser.quit()


