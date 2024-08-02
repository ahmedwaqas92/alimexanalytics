import sys
sys.path.append("../../")
from libraries.libraries import *
from schema.connectionstring.connection import databaseString

class loginSystem():
    def __init__(self):
        pass
    def errorHandling():
        error_messages = {
            "account":"Username or Email Does Not Exist",
            "authentication":"Incorrect Password"
        }
        return error_messages
    def hashFunction(credential):
        hash_object = hashlib.sha256()
        hash_object.update(str(credential).encode("utf-8"))
        encryption = hash_object.hexdigest()
        return encryption
    def userLogin(username_email, password):
        connectionString = sqlite3.connect(databaseString)
        link = connectionString.cursor()
        link.execute("SELECT * FROM users WHERE username='" + str(username_email) + "'")
        username_data = link.fetchall()
        if not username_data:
            link.execute("SELECT * FROM users where email='" +str(username_email) + "'")
            email_data = link.fetchall()
            if not email_data:
                error = loginSystem.errorHandling()
                return error["account"]
            else:
                encrpted_pass = loginSystem.hashFunction(password)
                for item in email_data:
                    if encrpted_pass == item[3]:
                        sessionData = {
                            "id":item[0],
                            "username":item[1],
                            "email":item[2],
                            "category":item[4],
                            "fname": item[5],
                            "lname": item[6]
                    }
                        return sessionData
                    else:
                        error = loginSystem.errorHandling()
                        return error["authentication"]
        else:
            encrpted_pass = loginSystem.hashFunction(password)
            for item in username_data:
                if encrpted_pass == item[3]:
                    sessionData = {
                        "id":item[0],
                        "username":item[1],
                        "email":item[2],
                        "category":item[4],
                        "fname": item[5],
                        "lname": item[6]
                    }
                    return sessionData
                else:
                    error = loginSystem.errorHandling()
                    return error["authentication"]
        connectionString.close()
