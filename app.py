from flask import Flask

# public variable with __

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello From Flask App"


if __name__ == "__main__":
    app.run()
