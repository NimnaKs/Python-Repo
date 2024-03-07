import mysql.connector as con

db = con.connect(
    host="localhost",
    port="3306",
    user="root",
    password="ijse@200108"
)
mycursor = db.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS uoc")
mycursor.close()


