from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello World!</h1>" * 10


@app.route("/test")
def hello_world2():
    return "Kura Labs"


if __name__ == "__main__":
    app.run(debug=True)