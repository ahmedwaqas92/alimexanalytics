import sys
sys.path.append("../../")
from libraries.libraries import *
from processes.dashboarddefaults.defaults import dashboardDeafults

dashboard_main = Blueprint("dashboard_main", __name__, static_folder="static", template_folder="templates")


@dashboard_main.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "username" in session:
        dropdowndata = dashboardDeafults.partDropDown()
        start_date = str((datetime.now() - timedelta(days=15)).strftime('%Y-%m-%d'))
        end_date = str(datetime.now().strftime('%Y-%m-%d'))
        cardData = dashboardDeafults.dataCards(start_date, end_date, partnames=dashboardDeafults.partDropDown())[0]
        graphingData = dashboardDeafults.dataCards(start_date, end_date, partnames=dashboardDeafults.partDropDown())[1]
        if request.method == "POST":
            date_range = request.form.get("daterange")
            if date_range:
                start_date, end_date = date_range.split(" to ")
                start_date = str(datetime.strptime(start_date, '%Y-%m-%d')).split()[0]
                end_date = str(datetime.strptime(end_date, '%Y-%m-%d')).split()[0]
            else:
                start_date, end_date = None, None
            
            selected_parts = request.form.getlist("parts")
            
            cardData = dashboardDeafults.dataCards(start_date, end_date, selected_parts)[0]
            graphingData = dashboardDeafults.dataCards(start_date, end_date, selected_parts)[1]
            
            return render_template("dashboard.html", current_page="dashboard", dropdowndata=dropdowndata, totalworkorders=cardData["totalWorkOrders"], totalweight=cardData["totalWeight"], totalsalesorders=cardData["totalSalesOrders"], totalpurchaseorders=cardData["totalPurchaseOrders"], graphingData=graphingData, start_date=start_date, end_date=end_date)
            
        return render_template("dashboard.html", current_page="dashboard", dropdowndata=dropdowndata, totalworkorders=cardData["totalWorkOrders"], totalweight=cardData["totalWeight"], totalsalesorders=cardData["totalSalesOrders"], totalpurchaseorders=cardData["totalPurchaseOrders"], graphingData=graphingData, start_date=start_date, end_date=end_date)
    else:
        return redirect(url_for("login_main.login"))
    
    