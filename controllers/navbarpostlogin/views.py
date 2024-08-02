import sys
sys.path.append("../../")
from libraries.libraries import *

navbarpostlogin_main = Blueprint("navbarpostlogin_main", __name__, static_folder="static", template_folder="templates")

@navbarpostlogin_main.route("/navbarpostlogin", methods=["GET", "POST"])
def navbarpostlogin():
    return render_template("navbarpostlogin.html")