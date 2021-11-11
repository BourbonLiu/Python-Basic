from flask import Flask, render_template
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)


moment = Moment(app)
start_time = datetime(2018, 1, 31, 0, 0, 0)


@app.route('/')
def index():
    return render_template('flask_moment.html',
                           page_header="page_header",
                           current_time=datetime.utcnow(),
                           start_time=start_time)


if __name__ == "__main__":
    app.run(debug=True)
