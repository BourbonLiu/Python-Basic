from flask import Flask, render_template


app = Flask(__name__)


@app.route('/nmf<int:standalone>')
def null_master_fallback(standalone):
    standalone = None if standalone == 0 else standalone
    return render_template("nmf.html", standalone=standalone, page_header="123")


if __name__ == "__main__":
    app.run(debug=True)
