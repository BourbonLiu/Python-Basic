from flask import Flask, render_template, request, url_for
from flask_moment import Moment
from datetime import datetime
import os
import uuid
import recognition.load_model as model


app = Flask(__name__)
moment = Moment(app)


UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + r'\static\uploaded'
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
        file = request.files['file']
        if file:
            filename = str(uuid.uuid4())+"_"+file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            predict = model.recog_digit(filename)
        return render_template('recog_result.html', page_header="Image Recognition", predict=predict, src=url_for('static', filename=f'uploaded/{filename}'))




if __name__ == "__main__":
    app.run(debug=True)
