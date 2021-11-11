from prompt_toolkit.keys import Keys
from selenium import webdriver

driver_path = r"D:\LabCode\Python\chromedriver.exe"
url = "https://www.youtube.com/"
key = "天能"

browser = webdriver.Chrome(driver_path)
browser.implicitly_wait(10)
browser.get(url)

search = browser.find_element_by_xpath("//*[@id='search']")
search.send_keys(key)
button = browser.find_element_by_xpath('//*[@id="search-icon-legacy"]')
button.click()


rs = browser.find_element_by_xpath('//*[@id="contents"]/ytd-item-section-renderer')
titles = rs.find_elements_by_tag_name("h3")


if len(titles) > 10:
    for i in range(0,10):
        title = titles[i].find_element_by_tag_name("a")
        print(title.get_attribute("title"))
        print("============================")
else:
    for i in range(len(titles)):
        title = titles[i].find_element_by_tag_name("a")
        print(title.get_attribute("title"))
        print("============================")


browser.quit()