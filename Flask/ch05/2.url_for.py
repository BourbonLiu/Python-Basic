from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello!</h1>'


@app.route('/user/<name>')
def user(name):
    return render_template('delimiters.html', name_jinja=name)

# The map class stores all the URL rules and some configuration parameters.
# 透過url_map就可以查看這個Web App所有的url
@app.route('/url_for')
def test_urlfor():
    print(app.url_map)
    return render_template('url_for.html')


if __name__ == "__main__":
    app.run(debug=True)
