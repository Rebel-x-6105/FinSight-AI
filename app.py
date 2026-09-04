from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def home():

    project_name = "FinSight AI"

    return render_template(
        "home.html",
        project_name=project_name
    )


@app.route("/login", methods=["GET", "POST"])
def login():

    message = None
    submitted_email = None

    if request.method == "POST":

        submitted_email = request.form.get("email", "").strip()

        message = (
            "Login form received successfully. "
            "Real authentication will be added in a later phase."
        )

    return render_template(
        "login.html",
        message=message,
        submitted_email=submitted_email
    )


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
