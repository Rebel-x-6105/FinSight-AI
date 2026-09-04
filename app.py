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


@app.route("/register", methods=["GET", "POST"])
def register():

    message = None
    message_type = None

    submitted_name = ""
    submitted_email = ""

    if request.method == "POST":

        submitted_name = request.form.get("full_name", "").strip()
        submitted_email = request.form.get("email", "").strip()

        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if password != confirm_password:

            message = "Password and Confirm Password do not match."
            message_type = "error"

        else:

            message = (
                "Registration form received successfully. "
                "Account creation will be implemented when the database "
                "and authentication system are added."
            )

            message_type = "success"

    return render_template(
        "register.html",
        message=message,
        message_type=message_type,
        submitted_name=submitted_name,
        submitted_email=submitted_email
    )


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
