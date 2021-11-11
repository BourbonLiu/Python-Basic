from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver_path = r"D:\LabCode\Python\chromedriver.exe"
url = "https://hahow.in/group/programming?page=%d"
driver = webdriver.Chrome(driver_path)


for i in range(1, 6):
    url = f"https://hahow.in/group/programming?page={i}"
    html = driver.get(url)
    wait = WebDriverWait(driver, 120)
    element = wait.until(ec.presence_of_element_located((By.TAG_NAME, "h4")))

    items = driver.find_elements_by_tag_name("h4")
    for item in items:
        print(item.text)

driver.quit()