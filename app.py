from flask import Flask, render_template, request

# public variable with __

app = Flask(__name__)


@app.route("/")
def home():
    name = input("User please tell me your name: ")
    return render_template(
        "home.html", data={"name": name}
    )  # always send data in dictionary variable


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "POST":
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        result = int(num1) + int(num2)
        return render_template("results.html", answer={"result": result})
    else:
        return render_template("results.html", answer={"result": "None"})


if __name__ == "__main__":
    app.run(debug=True)
