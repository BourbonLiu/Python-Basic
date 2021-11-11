from flask import Flask, escape


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


# 使用escape()或HTML語法，HTML標籤不會被瀏覽器解析
@app.route('/escape')
def with_escape():
    return escape('<h1>With escape()</h1>')
    # return "&lt;h1&gt;Not with escape()&lt;/h1&gt;"
    

# 沒有使用escape()，HTML標籤會被瀏覽器解析，除非加上HTML語法
@app.route('/not_escape')
def not_with_escape():
    return '<h1>Not With escape()</h1>'

# debug=True(開發階段才會用，正式Web App不會打開debug mode)
# 1.會在出現錯誤時，讓程式碼錯誤訊息顯示在網頁上，而不是顯示網頁錯誤的訊息
# 2.修改程式碼造成網頁異動時，會自動重新啟動Web App，而不用重新手動關閉再啟動

if __name__ == '__main__':
    app.run(debug=True)
