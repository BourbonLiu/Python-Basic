from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


# 透過__name__ == '__main__'，就不用再去終端機建立環境變數進行操作
if __name__ == '__main__':
    app.run()
