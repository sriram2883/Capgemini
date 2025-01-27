import pymysql

# Open database connection
db = pymysql.connect(
    host="localhost",
    user="root",
    password="MYSQL"
)

c = db.cursor()
c.execute("drop database testdb")
db.close()
