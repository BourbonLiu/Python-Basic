from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello World</h1>"

# 當輸入的id_小於100時，會出現網頁內容 ; 大於100時，會出現404頁面
@app.route('/user/<int:id_>')
def get_user(id_):
    if id_ > 100:
        abort(404)
        
    return f'<h1>Hello, No.{id_}</h1>'


if __name__ == '__main__':
    app.run(debug=True)
