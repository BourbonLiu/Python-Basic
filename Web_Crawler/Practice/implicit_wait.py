import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException

driver_path = r"D:\LabCode\Python\chromedriver.exe"
url = "https://hahow.in/group/programming?page=%d"
driver = webdriver.Chrome(driver_path)


for i in range(1, 6):
    url = f"https://hahow.in/group/programming?page={i}"
    html = driver.get(url)
    driver.implicitly_wait(10)

    items = driver.find_elements_by_tag_name("h4")
    ignored_exceptions = (StaleElementReferenceException)

    for item in items:
        print(item.text)

driver.quit()