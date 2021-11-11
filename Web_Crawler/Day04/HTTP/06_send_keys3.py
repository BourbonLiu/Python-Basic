from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driverPath = r'D:\LabCode\Python\chromedriver.exe'
url = "https://github.com/login"


driver = webdriver.Chrome(driverPath)
driver.implicitly_wait(20)
driver.get(url)

username = "BourbonLiu"
password = "bourbon0553"

user = driver.find_element_by_css_selector("#login_field")
user.send_keys(username)
pwd = driver.find_element_by_css_selector("#password")
pwd.send_keys(password)
pwd.send_keys(Keys.ENTER)
# button = driver.find_element_by_css_selector("input.btn.btn-primary.btn-block")
# button.click()

ele = driver.find_element_by_xpath("/html/body/div[1]/header/div[3]/nav")
items = ele.find_elements_by_tag_name("a")
# print(len(items))

for i in range(1,5):
    print(items[i].text)
    print(items[i].get_attribute("href"))

driver.quit()
