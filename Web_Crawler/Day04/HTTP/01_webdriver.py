from selenium import webdriver
# 透過selenium就可以瀏覽器開啟網頁，減少被server阻擋的機率

driverPath = r'D:\LabCode\Python\chromedriver.exe'
url = "https://www.lccnet.com.tw/lccnet"

driver = webdriver.Chrome(driverPath)
driver.implicitly_wait(10)                 # implicitly_wait()如果沒有在時間內取得網頁元素會出現錯誤
# time.sleep(5)                            # sleep()就會強制休息5秒，不管是否以取得網頁元素
driver.get(url)

title = driver.title
print(title)

print("----------------------------------------------------------")

html = driver.page_source                  # 取得網頁HTML
print(html)

driver.quit()