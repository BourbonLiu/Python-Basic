import os
import requests
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
containers = rs.find_elements_by_id("dismissible")

images = []

if len(containers) > 10:
    for i in range(10):
        title = containers[i].find_element_by_tag_name("h3")
        print(title.text)
        times = containers[i].find_element_by_css_selector("#metadata-line > span:nth-child(1)")
        print(times.text)
        channel = containers[i].find_element_by_css_selector("#text > a")
        print('頻道網址:', channel.get_attribute("href"))
        img = containers[i].find_element_by_xpath('//*[@id="img"]')
        src = img.get_attribute("src")
        images.append(src)
        print("="*100)

else:
    for i in range(len(containers)):
        title = containers[i].find_element_by_tag_name("h3")
        print(title.text)
        times = containers[i].find_element_by_css_selector("#metadata-line > span:nth-child(1)")
        print(times.text)
        channel = containers[i].find_element_by_css_selector("#text > a")
        print('頻道網址:', channel.get_attribute("href"))
        img = containers[i].find_element_by_css_selector("#img")
        src = img.get_attribute("src")
        images.append(src)
        print("="*100)


dir = '../Images'
if os.path.exists(dir) == False:
    os.mkdir(dir)


for i in range(len(images)):
    picture = requests.get(images[i])
    file = open(os.path.join(dir, str(i+1)+".jpg"), "wb")
    for size in picture.iter_content(10240):
        file.write(size)
    file.close()


browser.quit()












