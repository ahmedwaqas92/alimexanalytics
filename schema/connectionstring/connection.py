import sys
sys.path.append("../../")
from libraries.libraries import *

script_dir = os.path.dirname(os.path.abspath(__file__))

try:
    databaseString = os.path.join(script_dir, "..", "database", "alimexanalytics.db")
    databaseString = os.path.abspath(databaseString)
    connectionString = sqlite3.connect(databaseString)
except sqlite3.OperationalError as e:
    print(f"Failed to open database file at {databaseString}. Error: {e}")