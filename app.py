from flask import Flask

app = Flask(__name__)
#32.49
@app.route("/")
def hello_world():
    return "templates\home.html"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)