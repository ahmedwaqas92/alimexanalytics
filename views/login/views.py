import sys
sys.path.append("../../")
from libraries.libraries import *
from processes.login.login import loginSystem

login_main = Blueprint("login_main", __name__, static_folder="static", template_folder="templates")

@login_main.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username_email = request.form["usernameInput"]
        password = request.form["passwordInput"]
        login_data = loginSystem.userLogin(username_email, password)
        if isinstance(login_data, dict):
            session["id"] = login_data["id"]
            session["username"] = login_data["username"]
            session["email"] = login_data["email"]
            session["fname"] = login_data["fname"]
            session["lname"] = login_data["lname"]
            return redirect(url_for("dashboard_main.dashboard"))
        else:
            return render_template("login.html", prompt=login_data)
    return render_template('login.html')