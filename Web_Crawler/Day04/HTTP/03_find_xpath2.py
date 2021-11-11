from selenium import webdriver

driverPath = r'D:\LabCode\Python\chromedriver.exe'
url = r'D:\LabCode\Python\Web_Crawler\Day04\HTML\xPath_4.html'

browser = webdriver.Chrome(executable_path=driverPath)
browser.get(url)

n1 = browser.find_element_by_xpath("//h1/span")
print('span          : ', n1.text)

n2 = browser.find_element_by_xpath("//h1")
print('h1          : ', n2.text)

n3 = browser.find_element_by_xpath("//h1")
print('textContent : ', n3.get_attribute('textContent'))

n4 = browser.find_element_by_xpath("//h1")
print('innerHTML : ', n4.get_attribute('innerHTML'))

n5 = browser.find_element_by_xpath("//h1")
print('outerHTML : ', n5.get_attribute('outerHTML'))

n6 = browser.find_element_by_xpath("//div[@id='Traveling']//a[contains(text(),'天瓏書局')]")
print('outerHTML : ', n6.get_attribute('outerHTML'))
print('href : ', n6.get_attribute('href'))

browser.quit()