import csv
import time
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# 目標URL網址
URL = "https://tw.hotels.com/"
# 搜尋條件
KEY = "台北巿" 
CHECKIN = "2021-02-14"
CHECKOUT = "2021-02-15"

driver = None

def start_driver():
    global driver
    print("啟動 WebDriver...")
    driver = webdriver.Chrome(r'D:\LabCode\Python\chromedriver.exe')
    driver.implicitly_wait(10)

def close_driver():
    global driver
    driver.quit()
    print("關閉 WebDriver...")
    
def get_page(url):
    global driver
    print("取得網頁...")
    driver.get(url)
    time.sleep(2)

def search_hotels(searchKey, checkInDate, checkOutDate):
    global driver
    # 找出表單的HTML元素
    searchEle = driver.find_elements_by_xpath('//input[contains(@id,"destination")]')
    checkInEle = driver.find_elements_by_xpath('//input[contains(@class,"check-in")]')
    checkOutEle = driver.find_elements_by_xpath('//input[contains(@class,"check-out")]')
    
    if searchEle and checkInEle and checkOutEle:    
        actions = ActionChains(driver)     # 關閉彈出框
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ENTER)
        actions.perform()
               
        searchEle[0].send_keys(searchKey)  # 輸入搜尋條件
        searchEle[0].send_keys(Keys.TAB)        
        checkInEle[0].clear()
        checkInEle[0].send_keys(checkInDate)
        checkOutEle[0].clear()
        checkOutEle[0].send_keys(checkOutDate)

        checkOutEle[0].send_keys(Keys.ENTER)  # 送出搜尋        
        
        time.sleep(15)
        menu = driver.find_elements_by_xpath('//*[@id="enhanced-sort"]/li[5]/a')
        if menu:
            actions = ActionChains(driver)    # 選排序選單
            actions.move_to_element(menu[0])
            actions.perform()
            # 找出價格從低至商排序
            price=driver.find_elements_by_xpath('//*[@id="sort-submenu-price"]/li[2]/a')
            if price:
                price[0].click()
                time.sleep(10)
                return True  
    return False
                                
def grab_hotels():
    global driver                
    # 使用lxml剖析HTML文件

    hotels = driver.find_elements_by_xpath('//*[@id="listings"]/ol')
    found_hotels = [["旅館名稱","價格","星級","評價"]]
    for hotel in hotels:
        hotelName = hotel.find_elements_by_xpath('.//h3/a')  #//*[@id="listings"]/ol/li[1]/article/section/div/h3
        if hotelName:
            hotelName = hotelName[0].text
        price = hotel.find_elements_by_xpath('.//div[@class="price"]/a//ins')
        #price = hotel.xpath('//*[@id="listings"]/ol/li[2]/article/section/aside/div[1]')
        if price:
            price = price[0].text.replace(",","").strip()
        else:
            price = hotel.find_elements_by_xpath('.//div[@class="price"]/a')
            if price:
                price = price[0].text_content().replace(",","").strip()
        rating = hotel.find_elements_by_xpath('// *[ @ id = "listings"] / ol / li[1] / article / section / div / div / div[1] / span')
        if rating:
            rating = rating[0].text
        comment = hotel.find_elements_by_xpath('//*[@id="listings"]/ol/li[1]/article/section/div/div/div[2]/strong')
        if comment:
            comment = comment[0].text


        item = [hotelName, price, rating,comment ]
        found_hotels.append(item)
    
    return found_hotels    

def parse_hotels(url, searchKey, checkInDate, checkOutDate):
    start_driver()
    get_page(url)
    # 是否成功執行旅館搜尋
    if search_hotels(searchKey, checkInDate, checkOutDate):    
        hotels = grab_hotels()
        close_driver()
        return hotels
    else:
        print("搜尋旅館錯誤...")
        return []

def save_to_csv(items, file):
    with open(file, "w+", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp)
        for item in items:
            writer.writerow(item)
        
if __name__ == '__main__':    
    hotels = parse_hotels(URL, KEY, CHECKIN, CHECKOUT)
    for hotel in hotels:
        print(hotel)
    save_to_csv(hotels, "hotels.csv")

