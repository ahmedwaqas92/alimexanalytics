import sys
sys.path.append("../../")
from libraries.libraries import *
from schema.connectionstring.connection import databaseString

class registeringUsers():
    def __init__(self):
        pass
    def errorHandling(self):
        error_messages = {
            "password": "Passwords do not match",
            "username": "Username is already taken, please try another username",
            "email": "Email is in use, please provide a different email address",
            "id": "User ID is in use, try again",
            "success": "User registered Successfully"
        }
        return error_messages
    def hashFunction(self, credential):
        hash_object = hashlib.sha256()
        hash_object.update(str(credential).encode("utf-8"))
        encryption = hash_object.hexdigest()
        return encryption
    def registerUser(self, uuid, username, email, password, confirm_password, category, fname, lname):
        if str(password) == str(confirm_password):
            connectionString = sqlite3.connect(databaseString)
            link = connectionString.cursor()
            link.execute("SELECT * FROM users WHERE id='" + str(uuid) + "'")
            uuid_data = link.fetchall()
            if not uuid_data:
                link.execute("SELECT * FROM users WHERE username='" + str(username) + "'")
                username_data =  link.fetchall()
                if not username_data:
                    link.execute("SELECT * FROM users WHERE email='" + str(email) + "'")
                    email_data = link.fetchall()
                    if not email_data:
                        encrypted_pass = registeringUsers.hashFunction(self, password)
                        link.execute("INSERT INTO users(id,username,email,password,category,fname,lname) VALUES(?,?,?,?,?,?,?)", (str(uuid), str(username), str(email), str(encrypted_pass), str(category), str(fname), str(lname)))
                        connectionString.commit()
                        error = registeringUsers.errorHandling(self)
                        connectionString.close()
                        return error["success"]
                    else:
                        error = registeringUsers.errorHandling(self)
                        return error["email"]
                else:
                    error = registeringUsers.errorHandling(self)
                    return error["username"]
            else:
                error = registeringUsers.errorHandling(self)
                return error["id"]
        else:
            error = registeringUsers.errorHandling(self)
            return error["password"]
        
result = registeringUsers().registerUser(uuid.uuid4(), "malcolm", "malcolm@alimex.com.my", "@Alimex2016", "@Alimex2016", "admin", "Malcolm", "Hohls")
print(result)