from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    print(type(name))                   # print的內容要在終端機執行才看得到
    return f'<h1>Hello,{name}!</h1>'    # return的內容會顯示在網頁上

    
if __name__ == '__main__':
    app.run(debug=True)
