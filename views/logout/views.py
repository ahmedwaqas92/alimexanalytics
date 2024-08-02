import sys
sys.path.append("../../")
from libraries.libraries import *

logout_main = Blueprint("logout_main", __name__, static_folder="static", template_folder="templates")

@logout_main.route("/logout")
def logout():
    if 'username' in session:
        session.pop('id', None)
        session.pop('username', None)
        session.pop('email', None)
        session.pop('fname', None)
        session.pop('lname', None)
        return redirect(url_for("login_main.login"))
    else:
        return redirect(url_for("login_main.login"))