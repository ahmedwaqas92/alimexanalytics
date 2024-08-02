import sys
sys.path.append("../../")
from libraries.libraries import *

profile_main = Blueprint("profile_main", __name__, static_folder="static", template_folder="templates")

@profile_main.route("/profile", methods=["GET", "POST"])
def profile():
    if "username" in session:
        return render_template("profile.html", current_page="profile")
    else:
        return redirect(url_for("login_main.login"))