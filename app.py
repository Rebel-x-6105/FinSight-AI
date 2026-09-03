from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():

    project_name = "FinSight AI"

    return render_template(
        "home.html",
        project_name=project_name
    )


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
