from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello!</h1>'

# render_template()會自動去"templates"這個目錄尋找HTML檔
@app.route('/user/<name>')
def user(name):
    return render_template('delimiters.html', name_jinja=name)


@app.route("/filter/<var>")
def test_filter(var):
    safe_var = "<h1>456</h1>"
    return render_template("filter.html", var_jinja=var, safe_var_jinja=safe_var)


@app.route('/if/<name>')
def user_if(name):
    if name == "Allen":
        return render_template('if.html', user_jinja=name)
    else:
        return render_template('if.html', user_jinja=None)


@app.route('/for')
def user_for():
    lines = ["line1", "line2", "line3"]
    return render_template('for.html', Lines=lines)


if __name__ == "__main__":
    app.run(debug=True)
