from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('moment.html',
                           page_header="page_header")


@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('404.html',
                           error_message=e,
                           page_header="Page Not Found",), 404


if __name__ == "__main__":
    app.run(debug=True)
