import sys
sys.path.append("../../")
from libraries.libraries import *
from processes.dashboarddefaults.defaults import dashboardDeafults

dashboard_main = Blueprint("dashboard_main", __name__, static_folder="static", template_folder="templates")


@dashboard_main.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "username" in session:
        dropdowndata = dashboardDeafults.partDropDown()
        cardData = dashboardDeafults.dataCards()[0]
        graphingData = dashboardDeafults.dataCards()[1]
        return render_template("dashboard.html", current_page="dashboard", dropdowndata=dropdowndata, totalworkorders=cardData["totalWorkOrders"], totalweight=cardData["totalWeight"], totalsalesorders=cardData["totalSalesOrders"], totalpurchaseorders=cardData["totalPurchaseOrders"], graphingData=graphingData)
    else:
        return redirect(url_for("login_main.login"))