import requests

url = 'https://www.kingstone.com.tw/basic/2018730513521?zone=book&lid=book_index_reserve'
htmlfile = requests.get(url)
htmlfile.raise_for_status()  # 400代表Client端請求訊息不正確


# 400 Client端請求訊息不正確
# 401 Client端請求訊息不被授權
# 402 Client端完成請求必須有回應
# 403 Client端被禁止使用此資源
# 404 Client端請求訊息不存在
# 405 Client端請求資源的方法不被許可
# 406 Client端不被接受