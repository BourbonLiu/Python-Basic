import requests
# 避免送出請求後server端回應時間過長影響程式執行，所以用timeout設定請求時間
try:
    r = requests.get("http://www.google.com", timeout=0.03)
    print(r.text)
except requests.exceptions.Timeout as ex:
    print("錯誤: HTTP請求已經超過時間...\n" + str(ex))
