from flask import Flask, make_response

app = Flask(__name__)


@app.route('/')
def index():
    response = make_response('<h1>Check the status code</h1>')
    response.status_code = 200
    print(f"response.content_length : {response.content_length}",
          f"\nlen(\"<h1>Check the status code</h1>\") : {len('<h1>Check the status code</h1>')}")
          
    return response


if __name__ == '__main__':
    app.run(debug=True)
