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
        data = [item[0] for item in response]
        return data
    


