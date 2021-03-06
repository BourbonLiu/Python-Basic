from flask import Flask, render_template, request
from flask_moment import Moment
from datetime import datetime
import os
import uuid

app = Flask(__name__)
moment = Moment(app)

# 定義UPLOAD_FOLDER為目前路徑(現在這個檔案)+上uploaded目錄
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + r'\uploaded'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB


@app.route('/')
def index():
    return render_template('index.html',
                           page_header="page_header",
                           current_time=datetime.utcnow())


@app.route('/file', methods=['GET', 'POST'])
def get_file():
    if request.method == "GET":
        return render_template('file.html', page_header="upload file")

    elif request.method == "POST":
        # key is the value of name(html attribute) in <input type="file">
        file = request.files['file']
        if file:
            filename = str(uuid.uuid4()) + "_" + file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        data = [["method:", request.method],
                ["base_url:", request.base_url],
                ["file:", request.files]]
        return render_template('form_result.html', page_header="review file", data=data)


if __name__ == "__main__":
    app.run(debug=True)
