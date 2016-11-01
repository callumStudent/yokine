import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sqlalchemy
from numpy import genfromtxt

# Settings
db_name = "yokine"
username = "yokinearchers"
password = "VGKKpxGXoCrXyHTRYcFN"
db_uri = "mysql+mysqldb://%s:%s@yokinearchers.mysql.pythonanywhere-services.com/" % (username, password)

# Pull data from textfile
filename = "mysqltest.txt"
data = genfromtxt(filename,delimiter="\r\n",dtype=None)

# Create engine
engine = sqlalchemy.create_engine(db_uri, pool_recycle=280)
# Create connection
conn = engine.connect()
# Run commands
conn.execute("USE yokinearchers$yokine;")

with conn.begin() as trans:
    for news_post in data:
        conn.execute("INSERT INTO news(title,date,content,category_id) VALUES("
            +news_post+");")

# Close connection
conn.close()
