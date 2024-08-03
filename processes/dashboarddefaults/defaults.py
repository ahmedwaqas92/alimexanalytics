import sys
sys.path.append("../../")
from libraries.libraries import *
from schema.connectionstring.connection import databaseString

class dashboardDeafults():
    def __init__(self):
        pass
    def partDropDown():
        connectionString = sqlite3.connect(databaseString)
        link = connectionString.cursor()
        link.execute("SELECT DISTINCT part_name from workorders")
        response = link.fetchall()
        connectionString.close()
        data = [item[0] for item in response]
        return data
    def fetchWorkOrder(startdate, enddate, partnames):
        connectionString = sqlite3.connect(databaseString)
        connection = connectionString.cursor()
        placeholders = ', '.join('?' for _ in partnames)
        fetchQuery = f"""SELECT work_order, part_name, quantity, so_num, po_num, width, length, thickness, weight FROM workorders WHERE DATE(time_created_24h) BETWEEN ? AND ? AND part_name IN ({placeholders})"""
        connection.execute(fetchQuery, (startdate, enddate, *partnames))
        workorder_results = connection.fetchall()
        connectionString.close()
        return workorder_results
    def dataCards(startdate, enddate, partnames):
        cardData = {
            "totalWorkOrders": 0,
            "totalWeight": 0,
            "totalSalesOrders": 0,
            "totalPurchaseOrders": 0,
        }
        
        graphingData = []
        forCardValues = dashboardDeafults.fetchWorkOrder(startdate, enddate, partnames)
        graphingData.clear()
        
        for row in forCardValues:
            if row[0]:
                cardData["totalWorkOrders"] += 1
                if row[8]:
                    cardData["totalWeight"] += round(float(row[8]))
                if row[3]:
                    cardData["totalSalesOrders"] += 1
                    if row[4]:
                        cardData["totalPurchaseOrders"] += 1
                        tabulationData = {
                        "workOrder": row[0],
                        "partname": row[1],
                        "quantity": row[2],
                        "width": row[5],
                        "length": row[6],
                        "thickness": row[7],
                        "weight": row[8],
                        }
                        graphingData.append(tabulationData)
        
        return cardData, graphingData