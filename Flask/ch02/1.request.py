from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index():
    url = request.url
    return f'<h1>link is {url}</h1>'


@app.route('/user/allen')
def index2():
    url = request.url
    return f'<h1>link is {url}</h1>'


if __name__ == '__main__':
    app.run(debug=True)
