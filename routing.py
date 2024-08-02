from libraries.libraries import *
from views.login.views import login_main
from views.logout.views import logout_main
from controllers.navbarpostlogin.views import navbarpostlogin_main
from views.dashboard.views import dashboard_main
from views.reports.views import reports_main
from views.profile.views import profile_main

app = Flask(__name__)
app.debug = True
app.secret_key = "@l!mex@cp@$!@$dnbhd"

app.register_blueprint(login_main, url_prefix="/")
app.register_blueprint(logout_main, url_prefix="/")
app.register_blueprint(navbarpostlogin_main, url_prefix="/")
app.register_blueprint(dashboard_main, url_prefix="/")
app.register_blueprint(reports_main, url_prefix="/")
app.register_blueprint(profile_main, url_prefix="/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)