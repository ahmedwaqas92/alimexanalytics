import sys
sys.path.append("../../")
from libraries.libraries import *

reports_main = Blueprint("reports_main", __name__, static_folder="static", template_folder="templates")

@reports_main.route("/reports", methods=["GET", "POST"])
def reports():
    if "username" in session:
        return render_template("reports.html", current_page="reports")
    else:
        return redirect(url_for("login_main.login"))