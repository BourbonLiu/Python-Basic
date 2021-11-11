import requests

url_params = {'name': '陳聯成', 'score': 95}
htmltext = requests.get("http://httpbin.org/get", params=url_params)
print(htmltext.url)

# 並透過下列網址可以將得到的網頁原始碼進行decode得到傳遞參數的內容
# http://httpbin.org/get?name=%E9%99%B3%E8%81%AF%E6%88%90&score=95