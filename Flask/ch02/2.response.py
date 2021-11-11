from flask import Flask, request


app = Flask(__name__)


# 請求到該頁面時，會被回傳該訊息並狀態為404
@app.route('/')
def index():
    url = request.url
    return f'<h1>link is {url}</h1>', 404, {"key": 100, "key": 200}


if __name__ == '__main__':
    app.run(debug=True)
