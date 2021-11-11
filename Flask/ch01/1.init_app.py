from flask import Flask

# 第一步.創建Flask實例
# __name__ is the name of the current Python module. The app needs to know where it’s located to set up some path
app = Flask(__name__)               


# 第二步.創建一個路由及function
@app.route('/')
def index():
    return '<h1>Hello Python</h1>'

# 第三步.執行這支Web App
# 在終端機中建立環境變數set FLASK_APP=1.init_app.py
# flask run